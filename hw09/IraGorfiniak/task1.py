import random

user_name = input("Hi user, What is your name? \n")

number = random.randint(1, 100)

print(number)
counter = 0
max_attempts = 10
print(f"{user_name},You have {max_attempts} tries to guess the number. Lets start!")

while counter < max_attempts:
    counter += 1

    guess_number = int(input("Enter your number from range: 1 to 40:\n"))

    if 1 <= guess_number <= 100 and guess_number < number:
        print(f"{user_name}, your number is less")

    elif 1 <= guess_number <= 100 and guess_number > number:
        print(f"{user_name}, your number is more")

    elif not 1 <= guess_number <= 100:
        print(f"{user_name}, your number is not in range from 1 to 40")

    elif guess_number == number:
        print(f"You entered winning number in {counter} tries.")
        break
    print(max_attempts - counter, "attempts left")

if counter == max_attempts:
    print("Sorry, You have no tries")