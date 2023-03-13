from hw08_task3 import *

user_choice = input("Please choose area of which figure you want to calculate: ")
if user_choice == "Rectangle":
    rectangle_width = int(input("Please enter width value: "))
    rectangle_length = int(input("Please enter length value: "))
    print(rectangle_area(rectangle_width, rectangle_length))
elif user_choice == "Triangle":
    triangle_height = int(input("Please enter height value: "))
    triangle_base = int(input("Please enter base value: "))
    print(triangle_area(triangle_height, triangle_base))
elif user_choice == "Circle":
    circle_radius = int(input("Please enter radius value: "))
    print(circle_area(circle_radius))
else:
    print("Error, incorrect input! Please enter 'Rectangle', 'Triangle' or 'Circle'")
