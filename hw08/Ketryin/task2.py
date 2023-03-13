# Task2.
# Write a Python program to check the validity of a password (input from users).

import re

def validate_password(password):
    return re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@])[A-Za-z\d#$@]{6,16}$', password)

password = input("Enter password: ")
if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")