'''Check if the list contains odd numbers.
(Hint: use the break statement)'''

list = [2, 4, 6, 7, 8, 10]
odd = False

for i in list:
        if i % 2 != 0:
            odd = True
            break
if odd:
    print("The list contains odd numbers")
else:
    print("The list does not contain odd numbers")