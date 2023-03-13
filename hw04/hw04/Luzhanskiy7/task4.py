from math import factorial
number = int(input('Enter a number: '))
if number < 0:
    print('Error!!! your number is less than zero')
else:
    fac = factorial(number)
    print(fac)