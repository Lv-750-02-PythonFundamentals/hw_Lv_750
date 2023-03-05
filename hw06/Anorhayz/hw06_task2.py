user_login = input("Enter your login: ")
correct_login = "First"

while user_login != correct_login:
    print("Incorrect login, try again")
    user_login = input("Please enter your login: ")
else:
    print("Login is confirmed")
