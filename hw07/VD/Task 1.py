"""Write a function that returns the largest number of two
numbers
(use DocStrings documentation strings in the function).
"""

def largest(n1, n2):
    """This fuction accept 2 numbers n1 & n2 and return the largest value"""
    return max([n1, n2])

print(largest(2, 50))
print(largest(0, -50))
print(largest(50, 50))