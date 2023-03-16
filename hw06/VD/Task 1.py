# Task1. In the range from 1 to 10 determine
# • even numbers that are divisible by 2,
# • odd numbers, which are divisible by 3,
# • numbers that are not divisible by 2 and 3

lst = [i for i in range(1,11)]
print(lst)
lst_2 = [i for i in lst if i % 2 == 0]
print(lst_2)
lst_3 = [i for i in lst if i % 3 == 0 and i % 2 != 0]
print(lst_3)
lst_2_3 = [i for i in lst if i % 3 != 0 and i % 2 != 0]
print(lst_2_3)