def area_of_rectangle(a=1, b=1):
    print('Area of rectangle')
    a = int(input('Enter the length: '))
    b = int(input('Enter the width: '))
    print('S = ', a * b)

def area_of_triangle(a=1, b=1, c=1):
    print('Area of triangle')
    print('Enter the values of the lengths of the sides of the triangle:')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))

    p = (a+b+c) * 0.5
    s = ((p*(p-a) * (p-b) * (p-c)) ** 0.5)
    print('S = {0:.2f}'.format(s))

def area_of_circle(r=1):
    print('Area of circle')
    r = int(input('Enter the radius: '))
    pi = 3.14
    s = pi * r ** 2
    print('S = {0:.2f}'.format(s))