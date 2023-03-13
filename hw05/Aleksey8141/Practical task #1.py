'''Print all even numbers less than 100
(write two variants of the code:
one using the while loop,
and
the other using the for loop).'''

number = 0
while number < 100:
    if number % 2 == 0:
        print(number)
    number += 1

for number in range(0, 100, 2):
    print(number)