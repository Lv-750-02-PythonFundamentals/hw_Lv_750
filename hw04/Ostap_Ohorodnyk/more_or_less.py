number_one = int(input("Enter first number: "))
number_two = int(input("Enter first number: "))
if number_one == number_two:
    print("the numbers are equal")
else:
    print("First number bigger then number two" if number_one > number_two else "Number two bigger then first number")