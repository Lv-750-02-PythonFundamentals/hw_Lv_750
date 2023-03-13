import re

invalid_inputs = 0
while invalid_inputs <= 5:
    if invalid_inputs == 5:
        print("Password is invalid. You're out of tries. Please contact our support.")
        break
    else:
        print("Password is invalid. Please try again.")
        invalid_inputs += 1
    
    password = input("Enter password: ")
    
    if (len(password) >= 6 and len(password) <= 16 and
        re.search("[a-z]", password) and
        re.search("[A-Z]", password) and
        re.search("[0-9]", password) and
        re.search("[$#@]", password)
    ):
        print("Password is valid")
        break
