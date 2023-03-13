from math import*
number=int(input('Input number:'))

if number >= 0:
    print(f"The factorial of {number} is {factorial(number)}")
else:
    print("Factorial of negative numbers is undefined.")