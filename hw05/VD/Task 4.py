# Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function)

list = [1, 123, 55, 68, 129, 2, 67, 235, 8]
print(list)
for i in range (len(list)):     # check element's type of the created list
    print(f"index {i} element {list[i]}", type(list[i]))

for i in range(len(list)):      # change every element by index into float
    list[i] = float(list[i])

print(list)
for i in range (len(list)):     # check after change elemetns into float
    print(f"index {i} element {list[i]}", type(list[i]))