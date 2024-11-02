import random

class Card:
	
	card_suits_names = ("spades", "hearts", "diamonds", "clubs")
	unicode_offsets = (0x1F0A1,0x1F0B1,0x1F0C1,0x1F0D1)
	card_numbers = "A23456789TJ-QK"

	def __init__(self, suit: str, number: str):
		'''Initialize a Card Type
           Parameters:
                   suit (string): Card Suit
                   number (string): Card Number
    		'''
		if suit not in Card.card_suits_names:
			raise ValueError("Incorrect Card Suit")
		if number not in Card.card_numbers:
			raise ValueError("Incorrect Card Number")
		
		self.suit = suit	
		self.number = number
		self.is_hidden = False

	def __str__(self) -> str:
		if self.is_hidden:
			self.is_hidden = False
			return chr(0x1F0A0)
		else:
			uni_repr = Card.unicode_offsets[Card.card_suits_names.index(self.suit)]
			return chr(uni_repr + Card.card_numbers.index(self.number))

	def flip_card(self):
		'''flip the card to hide/unhide it'''
		self.is_hidden = not self.is_hidden

class Deck:
	'''Class to Represent Deck of Cards'''
	def __init__(self):
		'''Initialize a Deck of Cards'''
		self.deck = []
		for suit in Card.card_suits_names:
			for card in Card.card_numbers:
				if card != "-":
					self.deck.append(Card(suit, card))

	def shuffle_deck(self):
		'''shuffles the Deck'''
		random.shuffle(self.deck)

	def draw_card(self) -> Card:
		'''draws a card from the deck and returns the Card'''
		return self.deck.pop()

PLAYER_MONEY = 5000

game_deck = Deck()
game_deck.shuffle_deck()

def get_card_value(card_number: str) -> int:
	'''
	Gets value of card number in BlackJack
	
	Parameters:
		card_number: string
	Returns:
		int
	'''
	if card_number in "TKQJ":
		return 10
	match card_number:
		case "A":
			print("What score should A add upto? (1/11)")
			match input(">"):
				case "1":
					return 1
				case "11":
					return 11
				case _:
					return 0
		case _:
			return int(card_number)

print("How much do you bet? (1-5000, or QUIT)")
player_bet = input(">")
if player_bet.isdigit():
	player_bet = int(player_bet)
	if player_bet > 5000:
		print("Maximum Bet Can be 5000")
		player_bet = 5000
else:
	exit()
player_cards = []
dealer_cards = []



player_score = 0
dealer_score = 0

for _ in range(2):
	dealer_cards.append(game_deck.draw_card())
	dealer_score += get_card_value(dealer_cards[-1].number)
	player_cards.append(game_deck.draw_card())
	player_score += get_card_value(player_cards[-1].number)

dealer_cards[1].flip_card()
hit_required = False
while True:

	print("DEALER: ", end="")
	for card in dealer_cards:
		print(card, end=" ")
	print()
	print("PLAYER: ", player_score)
	for card in player_cards:
		print(card, end=" ")
	print()

	if player_score > 21:
		print("Dealer Won!")
		print("You lost your bet!")
		PLAYER_MONEY -= player_bet
		print(f"Your Money: {PLAYER_MONEY}")
		break

	print("(H)it, (S)tand, (D)ouble down")
	match input(">"):
		case "H":
			hit_required = False
			player_card = game_deck.draw_card()
			player_cards.append(player_card)
			player_score += get_card_value(player_cards[-1].number)
			if dealer_score > 17:
				print("Dealer is taking no more cards")	
			else:
				dealer_cards.append(game_deck.draw_card())
				dealer_score += get_card_value(dealer_cards[-1].number)
		case "S":
			if hit_required:
				print("You must hit exactly one more time before standing")
				continue
			else:
				print("You stopped taking cards")
				
				print(f"Dealer Score: {dealer_score}")
				print(f"Player Score: {player_score}")

				if player_score < dealer_score:
					print("Player Won!")
					PLAYER_MONEY += player_bet
					print(f"Your Money: {PLAYER_MONEY}")
				else:
					print("Dealer Won!")
					PLAYER_MONEY -= player_bet
					print(f"Your Money: {PLAYER_MONEY}")

				break
		case "D":
			if player_bet * 2 > PLAYER_MONEY:
				print("Can't double bet as it exceeds players money")
			else:
				player_bet *= 2
				print(f"Your doubled your bet!: {player_bet}")
				dealer_cards.append(game_deck.draw_card())
				dealer_score += get_card_value(dealer_cards[-1].number)
				hit_required = True
		case _:
			print("(H)it, (S)tand, (D)ouble down") 
