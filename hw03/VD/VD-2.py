# A four-digit natural number is specified:
number = int(input("please enter 4-digit number: "))
print("you entered", number, end="\n\n")

# - find the product of the digits of this number
number_str = str(number)
digit0 = number_str[0]
digit1 = number_str[1]
digit2 = number_str[2]
digit3 = number_str[3]
print(f"product = {int(digit0) * int(digit1) * int(digit2) * int(digit3)}", end="\n\n")

# - write the number in reverse order
print(f"reverse is {number_str[::-1]}", end="\n\n")

# - in ascending order, you need to sort the numbers included in the given number
print(f'sorted is {"".join(sorted(number_str))}')
