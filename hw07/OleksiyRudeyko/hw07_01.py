def largest_of_two(num1, num2):
    if num1 > num2:
        return f"{num1} is larger than {num2}"
    return f"{num2} is larger than {num1}"

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print(largest_of_two(num1, num2))
