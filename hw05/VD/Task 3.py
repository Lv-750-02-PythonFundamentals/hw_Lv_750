# Check if the list contains odd numbers.
# (Hint: use the break statement)

## initilization of the list and checking if its numeric
digit = True
while True:
    print("Please enter 5 numbers which will form the list")
    a, b, c, d, e = input("1 number:"), input("2 number:"), input("3 number:"), input("4 number:"), input("5 number:")
    list = [a, b, c, d, e]
    for numb in list:
        if numb.isnumeric():
            continue
        else:
            digit = False
    if digit == True:
        break    
    else:
        print("Numbers only, please...")
print(f"Your list is {list}")

## check for odd numbers
for i in list:
    if not int(i) % 2:
        continue
    else:
        print(f"Defined odd number in the list: {i}")