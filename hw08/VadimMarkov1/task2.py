import re


def check_password():
    password = input("Enter password: ")
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$])\S{6,16}$"
    match = re.match(pattern, password)
    if match:
        print("Password is valid")
    else:
        print("Password is invalid")


if __name__ == "__main__":
    check_password()
