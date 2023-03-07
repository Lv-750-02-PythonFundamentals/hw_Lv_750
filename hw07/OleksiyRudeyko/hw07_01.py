def largest_of_two(num1, num2):
    """
    Returns the largest number of two numbers.
    
    Parameters:
    num1: the first number.
    num2: the second number.
    
    Checks:
    if num1 is larger than num2

    Returns:
    formatted string "num1 is larger than num2" if the condition is True
    otherwise returns formatted string "num2 is larger than num1"
    """
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    return f"{num2} is larger than {num1}"

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print(largest_of_two(num1, num2))
