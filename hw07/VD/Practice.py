"""Write a function that returns the arithmetic mean of any
number of numbers
"""

def arith_mean(*args: int):
    """Function takes any number of integer numbers and returns its arithmetic mean"""
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)

print(arith_mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))