"""main area"""
from models import *

flag = int(input("select from the list:\n1. Area of a circle \n2. Area of a triangle \n3. Area of a rectangle\n: "))

if flag ==1:
    r = int(input("enter the circle radius"))
    circle_area(r)
elif flag == 2:
    h = int(input("enter the height of the triangle: "))
    a = int(input("enter the side of the triangle: "))
    triangle_area(h, a)
elif flag ==3:
    a = int(input("enter side a"))
    b = int(input("enter side b"))
    rectangle_area(a, b)
else:
    print(" You have not selected anything from the list.")

