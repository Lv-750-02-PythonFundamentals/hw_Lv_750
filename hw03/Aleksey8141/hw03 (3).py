'''Interchange the values of two variables without using the third variable'''

a = int(input('a = '))
b = int(input('b = '))
a = a + b # 2+8=10
b = a - b # 10-8=2
a = a - b # 10-2=8
print('a =', a, 'b =', b)