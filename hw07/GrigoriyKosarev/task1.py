"""
Task1. Write a function that returns the largest number of two
numbers
(use DocStrings documentation strings in the function).
"""
the_largest_numer1 = lambda x,y: x if x > y else y
print(the_largest_numer1(13, 5))

def the_largest_numer2(x, y):
    """
    Function return the largest number
    :param x: value 1
    :param y: value 1
    :return: result, the largest number
    """
    if x > y:
        return x
    return y

print(the_largest_numer2(13, 5))