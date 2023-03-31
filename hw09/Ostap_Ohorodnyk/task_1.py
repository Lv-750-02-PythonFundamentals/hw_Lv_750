from random import randint

action = True
secret_number = randint(1, 100)
number_of_attempts = 10

print(f"Guess a number from 1 to 100. You have {number_of_attempts} tries. Good luck! ;-)")

while action:
    attempt = int(input("enter a number : \n"))
    if attempt == secret_number:
        print("That's right! You won! :-)")
        action = False
    elif attempt < secret_number:
        number_of_attempts -= 1
        print(f"Your number is less than guessed. You have {number_of_attempts}  attempts left")
    elif attempt > secret_number:
        number_of_attempts -= 1
        print(f"Your number is more than guessed. You have {number_of_attempts} attempts  left")
    if number_of_attempts == 0:
        print(f"You have finished the attempt list. the guessed number was {secret_number}")
        action = False


