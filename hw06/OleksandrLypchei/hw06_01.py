divisible_2 = [x for x in range(1, 10) if not x % 2]
divisible_3 = [x for x in range(1, 10) if x % 2 and not x % 3]
not_divisible = [x for x in range(1, 10) if x % 2 and x % 3]

print(divisible_2)
print(divisible_3)
print(not_divisible)
