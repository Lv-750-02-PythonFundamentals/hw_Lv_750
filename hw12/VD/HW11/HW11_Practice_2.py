"""2. Write a program that prompts the user to enter their age, and then displays a
message stating whether the age is even or odd. The program must provide the ability
to enter a negative number, and in this case generate an exception. The master code
should call a function that processes the information entered.
"""
def age(age):
    try:
        if age < 0:
            raise ValueError("C'mon, it's not true :)")
        if age % 2:
            print("it's odd")
        else:
            print("it's even")
    except ValueError as e:
        print(e)

age(int(input("Please enter your age: ")))