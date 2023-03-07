number = int(input("Enter the number: \n"))
factorial = 1
if number < 0:
    print("Factorial doesn't exist for negative numbers")
else:
    for i in range(1, number + 1):
        factorial = factorial * i
    print("The factorial of", number, "is", factorial)

