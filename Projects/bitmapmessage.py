ascii_art = """
...................................
*******   *****    *****  **    ** 
**       **      **       **    ** 
**       **      **       **    ** 
******   **      **       **    ** 
**       **      **       **    ** 
**       **      **       **    ** 
**        *****    *****   ******  
...................................
"""

print("Bitmap Message, by Al Sweigart al@inventwithpython.com")
print("Enter the message to display with the bitmap.")

user_message = input(">")

while len(user_message) == 0:
	print("Message Cannot be Empty!")
	user_message = input(">")

message_length = len(user_message)

for line in ascii_art.splitlines():
	i = 0
	while i < 68:
		if line[i:i+1] == "*" or line[i:i+1] == ".":
			print(user_message[(i % message_length):(i % message_length)+1], end="")
		else:
			print(end=" ")
		i += 1
	print()