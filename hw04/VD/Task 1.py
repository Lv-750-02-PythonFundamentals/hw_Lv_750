# Write a script, which of the two entered
# numbers will determine which of them is
# more and which is less. Take into account
# the case of equality of numbers.

numb_1, numb_2 = input("Please enter number 1: "), input("Please enter number 2: ")

if numb_1.isdigit() and numb_2.isdigit():
    print("Number 1 is bigger") if numb_1 > numb_2 else None
    print("Number 2 is bigger") if numb_2 > numb_1 else None
    print("Numbers are equal") if numb_1 == numb_2 else None
else:
    print("It seems you have entered not a number")