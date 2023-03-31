import re

user_password = input("Please enter your password: ")
password_check = 0

while True:
    if len(user_password) <= 6:
        password_check = -1
        break
    elif len(user_password) >= 16:
        password_check = -1
        break
    elif not re.search("[a-z]", user_password):
        password_check = -1
        break
    elif not re.search("[A-Z]", user_password):
        password_check = -1
        break
    elif not re.search("[0-9]", user_password):
        password_check = -1
        break
    elif not re.search("[$#@]", user_password):
        password_check = -1
        break
    else:
        password_check = 0
        print("Password is valid")
        break

if password_check == -1:
    print("Not valid password")
