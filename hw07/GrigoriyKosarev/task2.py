"""
Task2. Write a program that calculates the area of a rectangle,
triangle and circle
(write three functions to calculate the area, and call them in the
main program depending on the user's choice).
"""

def area_of_rectangle(a, b):
    return a * b
def area_of_triangle(a, h):
    return 0.5 * a * h
def area_of_circle(r):
    return 3.14 * r**2

print("Set word 'rectangle', 'triangle' or 'circle' to calculate area value")
value = input()

if value == "rectangle":
    print("Set a")
    a = int(input())
    print("Set b")
    b = int(input())
    print(f"area = {area_of_rectangle(a, b)}")
elif value == "triangle":
    print("Set a")
    a = int(input())
    print("Set h")
    h = int(input())
    print(f"area = {area_of_triangle(a, h)}")
elif value == "circle":
    print("Set r")
    r = int(input())
    print(f"area = {area_of_circle(r)}")
