# Task1. Write a function that returns the largest number of two
# numbers
# (use DocStrings documentation strings in the function).

def largest_number(num1, num2):
    """
    Returns the largest number of two numbers.
    
    Parameters:
    num1: the first number.
    num2: the second number.
    
    Checks:
    if num1 is larger or equal than num2
    Returns:
    Returns message whitch number is the largest 
    """
    if num1>num2:
        return f'{num1} is the largest'
    elif num2>num1:
        return f'{num2} is the largest'
    elif num1==num2:
        return f'Numbers one and two are equal'
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(largest_number(num1, num2))