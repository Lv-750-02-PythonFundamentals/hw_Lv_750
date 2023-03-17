from math import sqrt

def square_triangle(a, b, c):
    if a != 0 and b != 0 and c != 0:
        p = (a + b + c) / 2
        s2 = sqrt(p * (p - a) * (p - b) * (p - c))
        print('Площа трикутника = ', round(s2, 3))
    else:
        print('Сторона трикутника не може дорівнювати або бути меньшою за 0')
