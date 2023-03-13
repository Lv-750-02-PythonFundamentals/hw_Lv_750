# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3.

even_numbers = []
odd_numbers_div_3 = []
numbers_not_div_2_3 = []
for i in range(1, 10):
    if i % 2 == 0:
        even_numbers.append(i)
    elif i % 2 == 1 and i % 3 == 0:
        odd_numbers_div_3.append(i)
    else:
        numbers_not_div_2_3.append(i)
print(even_numbers)
print(odd_numbers_div_3)
print(numbers_not_div_2_3)