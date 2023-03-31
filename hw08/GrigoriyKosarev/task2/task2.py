"""
Write a Python program to check the validity of a password (input from users).
Validation :
    - At least 1 letter between [a-z] and 1 letter between [A-Z].
    - At least 1 number between [0-9].
    - At least 1 character from [$#@].
    - Minimum length 6 characters.
    - Maximum length 16 characters.
"""
import re

print("Set your password: ")
password = input()
result = re.match("([a-z][A-Z][0-9][$#@])", password)
if result == None:
    print("Validation error")
if (len(password) < 6 or len(password) > 16):
    print("Validation error")
