"""Write a Python program to check the validity of a password (input from users).
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.
"""

import re

while True:
    password = input("Please enter the password: ")

    if re.search(r"^.{6,16}$", password) and re.search(r".*[a-z]", password) and re.search(r".*[A-Z]", password) and re.search(r".*[@#$]", password):
        print("Password is OK")
        break
    else:
        print("Password is not OK, try another")

