from math import pi, pow


def rectangle_area(width, length):
    area_of_rectangle = width * length
    return area_of_rectangle


def triangle_area(height, base):
    area_of_triangle = 0.5 * height * base
    return area_of_triangle


def circle_area(radius):
    area_of_circle = pi * pow(radius, 2)
    return area_of_circle

