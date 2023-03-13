"""Create a module with functions of addition, subtraction,
multiplication, division. And in another module - calculator.py, it is
necessary to ask the user what action he wants to perform and
with what numbers and perform the necessary actions.
"""
import Practical as p
while True:
    print("Please choose operation you would like to proceed:", "  '+'", "  '-'", "  '*'", "  '/'", "  'Q' for quit", sep="\n")
    operation = input()
    inputs = []
    if operation == "Q":
        break
    elif operation == "+":
        func = p.addition
    elif operation == "-":
        func = p.substr
    elif operation == "*":
        func = p.multipl
    elif operation == "/":
        func = p.division
    cond = False
    while not cond:
        inputs.append(input("Enter numbers and '=' to proceed: "))
        if "=" in inputs:
            cond = True

    print(func(inputs))
    