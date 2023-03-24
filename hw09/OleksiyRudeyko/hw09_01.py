import random

number = random.randint(1,100)

tries_number = 1

while tries_number <= 10:
    guess_number = int(input(f"Enter your number from 1 to 100:\nTry #{tries_number} \n"))
    if guess_number == number:
        print("Good job! You won!")
        break
    if tries_number == 10:
        print("Unfortunately, you didn't guess. \nThat was your last chance. \nBetter luck next time!")
        break
    elif 1 <= guess_number <= 100 and guess_number < number:
        print("Your number is smaller. Try again!") 
        tries_number = tries_number + 1
    elif 1 <= guess_number <= 100 and guess_number > number:
        print("Your number is bigger. Try again!")
        tries_number = tries_number + 1
    else:
        print("Your number is not in range.")
        tries_number = tries_number + 1
        