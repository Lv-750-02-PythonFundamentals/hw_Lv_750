"""area of circle"""
from math import pi, pow

def circle_area(r):
    s = round(pi * pow(r, 2), 2)
    print(f"The area of circle = {s}")
    return s

