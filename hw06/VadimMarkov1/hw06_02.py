def greet():
    login = input("Enter your login: ")
    while login != "First":
        print("Error: login is wrong")
        login = input("Enter your login: ")
    print("Hello, First!")


if __name__ == "__main__":
    greet()
