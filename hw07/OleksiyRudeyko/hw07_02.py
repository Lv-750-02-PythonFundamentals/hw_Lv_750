import math

print("Choose the figure: ")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

def area_of_rectangle(lenght, width):
    return lenght * width

def area_of_triangle(base, height):
    return 1/2 * base * height

def area_circle(r):
    return round(math.pi * r ** 2, 2)

figure = int(input("Enter your choice: "))

if figure == 1:
    lenght = int(input("Enter lenght: "))
    width = int(input("Enter width: "))
    print(area_of_rectangle(lenght, width))
    
if figure == 2:
    base = int(input("Enter base: "))
    height = int(input("Enter height: "))
    print(area_of_triangle(base, height))

if figure == 3:
    r = int(input("Enter radius: "))
    print(area_circle(r))
