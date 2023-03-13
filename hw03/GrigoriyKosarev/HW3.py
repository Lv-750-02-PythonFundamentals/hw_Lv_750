from builtins import print

f = open("Zen.txt", "r")
zen_text = f.read()

"""
You need to write Python's philosophy in the string format:
- find separately the number of occurrences of the words
  "better", "never" and "is" in the given line
- you need to display all text in uppercase (all letters in uppercase)
- replace all occurrences of the symbol “i” with “&”
"""

better_count = zen_text.count("better")
never_count = zen_text.count("never")
is_count = zen_text.count("is")

print(f"better count: {better_count}")
print(f"never count: {never_count}")
print(f"is count: {is_count} ")

print(zen_text.upper())

print(zen_text.replace("i", "&"))

"""
A four-digit natural number is specified:
- find the product of the digits of this number
- write the number in reverse order
- in ascending order, you need to sort the numbers included in the given number
"""
digit_number = 1458
digit_number_str = str(1548)
list_number = list(digit_number_str)

product_digits = int(digit_number_str[0]) * int(digit_number_str[1])\
                 *int(digit_number_str[2]) * int(digit_number_str[3])
print(f"the product of the digits of this number: {product_digits}")

list_number_reverse = list(digit_number_str)
list_number_reverse.sort()
list_number_reverse.reverse()
print(f'reverse: {"".join(list_number_reverse)}')

list_number.sort()
print(f'sort: {"".join(list_number)}')

"""
Interchange the values of two variables without using the third variable.
"""
a = 1
b = 2

a, b = b, a
print(f"a= {a}, b= {b}")




