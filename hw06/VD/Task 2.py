# Task2. Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is
# different, send an error message.
# (need to use loop while)

login_user = {"First" : "VD"}
login = ""
while login != "First":
    login = input("Login: ")
else:
    print(f"Hello {login_user[login]}!")



