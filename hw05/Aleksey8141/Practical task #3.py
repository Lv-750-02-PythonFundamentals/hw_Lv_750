'''Check if the list contains odd numbers.
(Hint: use the break statement)'''

list = [2, 4, 6, 7, 8, 10]

for i in list:
        if i % 2 == 0:
            continue
        elif i % 2 != 0:
            print('The list contains odd numbers')
            break

