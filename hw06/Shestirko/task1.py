even_div_by_2 = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers that are divisible by 2:", even_div_by_2)

odd_div_by_3 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 == 0]
print("Odd numbers that are divisible by 3:", odd_div_by_3)

not_div_by_2_or_3 = [i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0]
print("Numbers that are not divisible by 2 and 3:", not_div_by_2_or_3)