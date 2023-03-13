"""
Create a list that contains elements of integer type, then
use the loop to change the type of these elements to a floating
type.
(Hint: use the built-in float () function).
"""

list_of_numbers = [1,2,3,4,5,6,7,8,9,0]
print(list_of_numbers)
i = 0
for el in list_of_numbers:
    list_of_numbers[i] = float(el)
    i += 1

print(list_of_numbers)