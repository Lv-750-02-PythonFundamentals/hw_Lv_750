"""
Write a program that calculates the area of a rectangle S=a*b, the area of a
triangle S=0.5*h*a, the area of a circle S=pi*r**2. This module must be used in
another module in which we ask the user the area of which figure he wants to
calculate.
(To perform the task, you need to import the math module, and from it the
pow() function and the value of the variable pi, and module, which contains
three functions for finding areas, into the main program. The basic logic of the
program is executed in the main module).
"""

from calc_area import area_triangle, area_rectangle, area_circle

print("What the area of figure you wont to calculate? (Enter triangle, circle or rectangle)")
figure = input()

if figure == "triangle":
    print("Set value h")
    h = int(input())
    print("Set value a")
    a = int(input())
    print(f"Area triangle = {area_triangle(h, a)}")
elif figure == "rectangle":
    print("Set value a")
    a = int(input())
    print("Set value b")
    b = int(input())
    print(f"Area rectangle = {area_rectangle(a, b)}")
elif figure == "circle":
    print("Set value r")
    r = int(input())
    print(f"Area rectangle = {area_circle(r)}")

