def rectangle():
    l = float(input("Enter the length of the rectangle: "))

    b = float(input("Enter the breadth of the rectangle: "))
    area = l*b

    print("Area of the rectangle =", area)


def triangle():
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))
    c = float(input("Enter third side: "))

    # calculate the semi-perimeter
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print("The area of the triangle is %0.2f" % area)


def circle():
    r = float(input("Enter the radius of the circle: "))
    area = 3.14 * (r * r)

    print("Area of the circle =", area)


print("Press 1 to calculate Area of Rectangle")

print("Press 2 to calculate Area of Triangle")

print("Press 3 to calculate Area of Circle")

f = int(input())

if f == 1:
    rectangle()


elif f == 2:
    triangle()


elif f == 3:

    circle()

else:

    print("Error 404: Wrong number pressed, cannot calculate area!")
