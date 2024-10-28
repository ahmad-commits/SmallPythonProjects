import random

MAX_GUESSES = 10
MAX_DIGITS = 3

game_intro = f"""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a {MAX_DIGITS}-digit number. Try to guess what it is.
Here are some clues:
When I say:      That means:
    Pico             One digit is correct but in the wrong position.
    Fermi            One digit is correct and in the right position.
    Bagels           No digit is correct."""

def generate_number() -> str:
	return str(random.randint(10**(MAX_DIGITS-1), 10**(MAX_DIGITS) - 1))

def check_guess(user_input, secret) -> str:
	i = 0
	result = ""
	while i < MAX_DIGITS:
		if user_input[i] == secret[i]:
			result += " Fermi"
		elif user_input[i] in secret:
			result += " Pico"
		i += 1
	if result == "":
		result = "Bagels"
	return result


print(game_intro)
secret_number = generate_number()
print("I have thought up a number.")
print(f" You have {MAX_GUESSES} guesses to get it.")

guess_number = 1

player_win = False
while guess_number <= MAX_GUESSES:
	print(f"Guess # {guess_number}")

	user_number = input("> ")

	if not user_number.isnumeric() or len(user_number) != MAX_DIGITS:
		print(f"Enter a {MAX_DIGITS} digits number.")
		continue
	elif user_number == secret_number:
		print("You got it!")
		player_win = True
		break
	else:
		print(check_guess(user_number, secret_number))

	guess_number += 1

if not player_win:
	print('You ran out of guesses.')
	print(f'The answer was {secret_number}.')