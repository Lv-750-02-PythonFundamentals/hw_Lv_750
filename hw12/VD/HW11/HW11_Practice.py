"""1. Write a program that prompts the user to enter an integer and determines whether
the number is even or odd, taking into account the case of entering incorrect data.
"""

run = 1
while run:
    try:
        number = int(input("Please enter integer number: "))
        if (number % 2):
            print("its odd")
        else:
            print("its even")
        run = 0

    except ValueError as error:
        print(error, "Please try again")
