from math import factorial

num = int(input("Enter your number: "))

if num < 0:
    print("Sorry, the factorial for negative numbers do not exist.")
else:
    print("The factorial of your number is:", factorial(num))
