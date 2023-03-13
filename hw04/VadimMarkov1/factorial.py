import math


def factorial(number: int):
    return math.factorial(number)


if __name__ == "__main__":
    try:
        user_number = int(input("Please enter number: "))
        print(f"Factorial of number {user_number} is {factorial(user_number)}")
    except ValueError:
        print("Please enter correct number")
