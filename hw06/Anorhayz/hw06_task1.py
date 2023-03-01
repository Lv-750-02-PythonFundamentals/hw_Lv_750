even_num = 0
odd_num = 0
rest_num = 0

for i in range(1, 11):
    if i % 2 == 0:
        even_num = i
        print("Even numbers are:", even_num)

for i in range(1, 11):
    if i % 3 == 0:
        odd_num = i
        print("Odd numbers are:", odd_num)

for i in range(1, 11):
    if i % 2 != 0 and i % 3 != 0:
        rest_num = i
        print("Numbers that are not divisible by 2 and 3:", rest_num)
