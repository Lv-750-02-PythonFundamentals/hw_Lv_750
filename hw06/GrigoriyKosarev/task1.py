
"""
Task1. In the range from 1 to 10 determine
• even numbers that are divisible by 2,
• odd numbers, which are divisible by 3,
• numbers that are not divisible by 2 and 3.
"""
divisible_by_2 = []
divisible_by_3 = []
not_divisible = []
for i in range(1, 10):
    if i % 2 == 0:
        divisible_by_2.append(i)
    else:
        if i % 3 == 0:
            divisible_by_3.append(i)

    if i % 2 != 0 and i % 3 != 0:
        not_divisible.append(i)

print(f"even numbers that are divisible by 2: {divisible_by_2}")
print(f"odd numbers, which are divisible by 3: {divisible_by_3}")
print(f"numbers that are not divisible by 2 and 3: {not_divisible}")