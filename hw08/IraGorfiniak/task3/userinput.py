from areacalculation import *

print("Press 1 to calculate Area of Rectangle")

print("Press 2 to calculate Area of Triangle")

print("Press 3 to calculate Area of Circle")

f = int(input())

if f == 1:
    a = float(input("Enter the length of the rectangle: "))

    b = float(input("Enter the breadth of the rectangle: "))

    print(f"Area of the rectangle =", area_of_rectangle(a, b))


elif f == 2:
    h = float(input("Enter triangle height: "))
    a = float(input("Enter triangle base: "))

    print(f"Area of the triangle =", area_of_triangle(h, a))


elif f == 3:

    r = float(input("Enter the radius of the circle: "))

    print(f"Area of the triangle =", area_of_circle(r))
else:

    print("Error 404: Wrong number pressed, cannot calculate area!")
