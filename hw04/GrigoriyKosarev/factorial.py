import math
from builtins import print

print("Insert int value to calculate factorial: ")
number = input()

print(f"Result 1: {math.factorial(int(number))}")

i = 0
fact = 1
while i <= int(number):
    if i > 1:
        fact = fact * i
    i += 1

print(f"Result 2: {fact}")

