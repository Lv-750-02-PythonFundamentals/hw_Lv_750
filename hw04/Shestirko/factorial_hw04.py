import math

n = int(input("Enter a number: "))

# Check if the number is non-negative
if n >= 0:
    factorial = math.factorial(n)
    print(f"The factorial of {n} is {factorial}")
else:
    # If the number is negative
    print("Factorial of negative numbers is undefined.")