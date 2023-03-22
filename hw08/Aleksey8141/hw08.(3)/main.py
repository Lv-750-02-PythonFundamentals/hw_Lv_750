from square import square_circle, square_triangle, square_rectangle

square = input('Площу якої фігури обчислюємо? \n')

if square == 'круг':
    square_circle(int(input('Введіть радіус круга = ')))
elif square == 'трикутник':
    square_triangle(int(input('a = ')), int(input('b = ')), int(input('c = ')))
elif square == 'прямокутник':
    square_rectangle(int(input('Сторона a = ')), int(input('Сторона b = ')))
else:
    print('Невірний ввід. Спробуйте ще раз.')
