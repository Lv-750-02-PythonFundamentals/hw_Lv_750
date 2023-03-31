divisible_by_two = [i for i in range(1, 10) if i % 2 == 0]
print(divisible_by_two)
odd_divisible_by_three = [i for i in range(1, 10) if i%2!=0 and i % 3 == 0]
print(odd_divisible_by_three)
not_divisible_by_two_and_three = [i for i in range(1, 10, 2) if i % 3 != 0]
print(not_divisible_by_two_and_three)
