from math import *

'''
S1 = pi * (r**2)  # площа круга
S2 = sqrt(p*(p-a)*(p-b)*(p-c)) # площа трикутника, де p=(a+b+c)/2
S3 = a*b # площа прямокутника
'''

def square():
    square = input('Площу якої фігури обчислюємо? \n')
    if square == 'круг':
        def square_circle(r):
            if r > 0:
                s1 = pi * (r ** 2)
                print('Площа круга =', round(s1, 2))
            else:
                print('Введіть радіус круга більший за 0')
        square_circle(int(input('Введіть радіус круга = ')))

    elif square == 'трикутник':
        def square_triangle(a, b, c):
            if a != 0 and b != 0 and c != 0:
                p = (a + b + c) / 2
                s2 = sqrt(p * (p - a) * (p - b) * (p - c))
                print('Площа трикутника = ', round(s2, 3))
            else:
                print('Сторона трикутника не може дорівнювати або бути меньшою за 0')
        square_triangle(int(input('a = ')), int(input('b = ')), int(input('c = ')))
    elif square == 'прямокутник':
        def square_rectangle(a, b):
            if a != 0 and b != 0:
                s3 = a * b
                print('Площа прямокутника =', s3)
            else:
                print('Сторона прямокутника не може дорівнювати або бути меньшою за 0')
        square_rectangle(int(input('Сторона a = ')), int(input('Сторона b = ')))
    else:
        print('Некоректна назва фігури')
square()


