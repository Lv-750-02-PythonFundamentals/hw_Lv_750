'''In the range from 1 to 10 determine
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3.'''


even_num = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers:", even_num)
odd_num = [i for i in range(1, 11) if i % 3 == 0]
print("Odd numbers:", odd_num)
other_num = [i for i in range(1, 11) if i % 2 != 0 and i % 3 != 0]
print("Numbers that are not divisible by 2 and 3:", other_num)