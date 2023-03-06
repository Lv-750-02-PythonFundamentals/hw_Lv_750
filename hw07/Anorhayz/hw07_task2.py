user_choice = input("Which area do you want calculate?(Rectangle, Triangle, Circle) ")


def rectangle_area(length, width):
    area_rectangle = length * width
    return area_rectangle


def triangle_area(base, height):
    area_triangle = (1/2) * base * height
    return area_triangle


def circle_area(radius):
    pi_value = 3.14
    area_circle = pi_value * radius**2
    return area_circle


if user_choice == "Rectangle":
    rectangle_length = int(input("Please enter length: "))
    rectangle_width = int(input("Please enter width: "))
    print(rectangle_area(rectangle_length, rectangle_width))
elif user_choice == "Triangle":
    triangle_base = int(input("Please enter base: "))
    triangle_height = int(input("Please enter height: "))
    print(triangle_area(triangle_base, triangle_height))
elif user_choice == "Circle":
    circle_radius = int(input("Please enter radius: "))
    print(circle_area(circle_radius))
else:
    print("Error! Enter only 'Rectangle', 'Triangle' or 'Circle'")
