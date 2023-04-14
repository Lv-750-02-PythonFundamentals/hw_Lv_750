"""Find the largest item in the list using the reduce function
"""
from functools import reduce

lst = [10, 152, 35, 1, 80, 0, 156, -5, 56]

def largest_number(a, b):
    if a - b >= 0:
        largest = a
    else:
        largest = b
    return largest

print(reduce(largest_number, lst))

