import random

MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

MONTHS_AND_DAYS = {
"Jan": 31,
"Feb": 28,
"Mar": 31,
"Apr": 30,
"May": 31,
"Jun": 30,
"Jul": 31,
"Aug": 31,
"Sep": 30,
"Oct": 31,
"Nov": 30,
"Dec": 31,
}

class Birthday:
	def __init__(self, day, month):
		self.day = day
		self.month = month

	def __str__(self):
		return f"{self.day} {self.month}"

	def get_day(self):
		return self.day

	def get_month(self):
		return self.month

	@staticmethod
	def gen_birthday():
		chosen_month = random.choice(MONTHS)
		max_days = MONTHS_AND_DAYS[chosen_month]
		chosen_day = random.randint(1, max_days)
		return Birthday(chosen_day, chosen_month)


print("Birthday Paradox, by Al Sweigart al@inventwithpython.com")
print("How many birthdays shall I generate? (Max 100)")

birthdays_count = input(">")

while not birthdays_count.isnumeric():
	print("please enter a number")
	birthdays_count = input(">")

birthdays_count = int(birthdays_count)

print(f"Here are {birthdays_count} birthdays:")

generated_birthdays = []

i = 0
while i < birthdays_count:
	generated = Birthday.gen_birthday()
	print(generated, end=", ")
	generated_birthdays.append(generated)
	i += 1
print()


frequency = {}
for birthday in generated_birthdays:
	if f"{birthday}" not in frequency.keys():
		frequency[f"{birthday}"] = 1
	else:
		frequency[f"{birthday}"] += 1

for birthday, freq in frequency.items():
	if freq > 1:
		print(f"In this simulation, multiple people have a birthday on {birthday}")

print(f"Generating {birthdays_count} random birthdays 100000 times...")
input("Press Enter to begin...")

i = 0
count = 0
frequency = {}
while i < 100000:
	frequency = {}
	for _ in range(birthdays_count):
		generated = Birthday.gen_birthday()
		if f"{generated}" in frequency.keys():
			count += 1
			break
		else:
			frequency[f"{generated}"] = 1
	if i % 10000 == 0:
		print(f"{i} simulations run")
	i += 1

print(f"""Out of 100,000 simulations of {birthdays_count} people, there was a
matching birthday in that group {count} times. This means
that {birthdays_count} people have a {round(100*count/100000, 2)} % chance of
having a matching birthday in their group.
That's probably more than you would think!""")