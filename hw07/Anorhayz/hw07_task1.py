user_number_1 = input("Enter your first number: ")
user_number_2 = input("Enter your second number: ")


def max_numbers(user_number1, user_number2):
    """ This function returns the largest number of two numbers"""
    if user_number1 > user_number2:
        print(user_number1)
    else:
        print(user_number2)


print(max_numbers.__doc__)
max_numbers(user_number_1, user_number_2)
