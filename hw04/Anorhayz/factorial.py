user_number = int(input("Please enter your number: "))

factorial = 1

if user_number < 0:
    print("Error! Factorial must be 0 or positive number")
elif user_number == 0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, user_number+1):
        factorial = factorial*i
    print(f"Factorial of { user_number } is { factorial }")
