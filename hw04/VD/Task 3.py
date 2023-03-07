# Write a script that will calculate the
# factorial of the entered number without using
# recursion.
from math import factorial

fact_number = input("Please enter a factorial number: ")
if fact_number.isdigit():
    
    print(f"Factorial of the entered number is {factorial(int(fact_number))}")
    
