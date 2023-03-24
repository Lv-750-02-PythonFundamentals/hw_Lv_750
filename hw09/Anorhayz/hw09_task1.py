from random import randint

random_num = randint(1, 100)
guess_attempt = 0

for i in range(10):
    user_guess = int(input("Please enter the number from 1 to 100: "))
    if user_guess > random_num:
        print("Your number is more, try again")
        guess_attempt += 1
    elif user_guess < random_num:
        print("Your number is less, try again")
        guess_attempt += 1
    elif user_guess == random_num:
        print("Congratulations, you guessed the number")
        break
    else:
        print("Your attempts ended")
