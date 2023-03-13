number = 285
digit = number
product = 1

while digit != 0:
    product = product * (digit % 10)
    digit = int(digit / 10)

    reversed_number = int(str(number)[::-1])

print("\nProduct of all digits in", number, ":", product)
print("\n Reversed number is: " + str(reversed_number))
print("\nSorted:", sorted(str(number)))
