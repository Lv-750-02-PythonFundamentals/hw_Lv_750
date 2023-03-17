'''Write a Python program to check the validity of a password (input from users).
Validation :
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters'''

password = input('Введіть пароль:')

cond1 = len(password) >= 6 <= 16
cond2 = not password.islower() and not password.isupper()
cond3 = len({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} & set(password)) > 0
cond4 = len({'@', '#', '%', '&'} & set(password)) > 0

if cond1 and cond2 and cond3 and cond4:
    print('Пароль достатньо надійний')
else:
    print('Надійність пароля недостатня')
