num = int(input("Enter 4-digit number: "))

# Decompose number into 4 digits
digit1 = num % 10
digit2 = num % 100 // 10
digit3 = num % 1000 // 100
digit4 = num // 1000
print(digit1, digit2, digit3, digit4)

product = digit1 * digit2 * digit3 * digit4
print(f"Product of digits - {product}.")

reversed_num = digit4 + digit3*10 + digit2*100 + digit1*1000
print(f"Number in reverse - {reversed_num}.")

list_od_digits = [digit1, digit2, digit3, digit4]
list_od_digits.sort()
sorted_num = list_od_digits[3] + list_od_digits[2]*10 + list_od_digits[1]*100 + list_od_digits[0]*1000
print(f"Number with sorted digits - {sorted_num}.")
