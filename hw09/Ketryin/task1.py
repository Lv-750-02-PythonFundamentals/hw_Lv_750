# Task 1. Write a game script that randomly generates a number from a range of
# 1 to 100 and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user and prompts the user
# whether the guessed number is greater or less than the number entered by the
# user. The game must continue until the user has used 10 attempts and guessed
# the number. If the user guessed the number, the program prints a
# congratulatory message, and if 10 attempts have been exhausted and the user
# did not have time to guess the number, then the corresponding message is
# displayed.
# (to perform the task, you need to import the random module,
# and from it the randint() function)
import random
number=random.randint(1,100)
counter=0

while True:
	guess_number=int(input("Enter your number from range: 1 to 100: "))
	if guess_number == number:
		print('Good job! You are a winner!!!')
		break
	if counter == 10:
		break
	elif 1 <= guess_number <= 100 and guess_number < number:
		print('Your number is less.') 
		counter=counter + 1
	elif 1 <= guess_number <= 100 and guess_number > number:
		print('Your number is more.')
		counter=counter + 1
	elif not 1 <=guess_number <= 100:
		print(f"Your number is not in the range 1 to 40. Try again:)")
		counter=counter + 1

