'''Print all odd numbers less than 100.
(write two versions of the code:
one using the continue operator,
and
the other without this operator)'''

for i in range(1, 100):
    if i % 2 == 0:
        continue
    print(i)

for i in range(1, 100):
    if i % 2 != 0:
        print(i)

