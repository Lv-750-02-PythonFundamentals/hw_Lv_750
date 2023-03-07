# Task2. Write a program that calculates the area of a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).
import math

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return (base * height) / 2

def area_circle(r):
    return math.pi * r ** 2

print("Choose the figure: ")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

figure = input("Enter number of figure: ")
if figure == '1':
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    print(f'Area of rectangle:{area_rectangle(length, width)}')
    
if figure == '2':
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    print(f'Area of triangle:{area_triangle(base, height)}')

if figure == '3':
    r = int(input("Enter radius: "))
    print(f'Area of circle:{area_circle(r)}')