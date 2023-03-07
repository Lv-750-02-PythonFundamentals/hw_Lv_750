import math


num = input("Enter number: ")

# Checking if number is float
if not num.isdigit():
    print("Your number is not integer. Try integer number!")
else:
    num = int(num)
    # Checking if number is negative
    if num < 0:
        print("Your number is negative! Try positive number!")
    else:
        print(f"Factorial of your number is {math.factorial(num)}")
