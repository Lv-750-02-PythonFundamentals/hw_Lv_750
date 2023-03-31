
logins = ["login1", "login2"]

while True:
    print("Enter login: ")
    login = input()
    if logins.count(login) == 0:
        logins.append(login)
        print(f"Hello, {login}!")
        break
    else:
        print("user with this login already exists")
