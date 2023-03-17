from math import pi

def square_circle(r):
    if r > 0:
        s1 = pi * (r ** 2)
        print('Площа круга =', round(s1, 2))
    else:
        print('Введіть радіус круга більший за 0')
