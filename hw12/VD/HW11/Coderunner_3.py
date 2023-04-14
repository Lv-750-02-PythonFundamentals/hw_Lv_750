"""Write code inside function check.

This function must check logins of some workers. We have 2 roles: there are "admin" and "employee", each login must contain role and id.

Id is any natural number. Id and role may be separated by "-" or "-id" or "id".

If function check obtain incorrect data (as example 'abc') it needs to raise ValueError with message "incorrect login 'abc'". Note that all data may be case-insensitive.
"""

import re


def check(login):
    
    if re.search(r"^(?:employee|admin)(?:-|id|-id)(?:\d+)$", login.lower()):
        return True
    else:
        raise ValueError(f"incorrect login '{login}'")
    


from random import choices
from string import ascii_letters, digits

letters_and_digits = choices(ascii_letters, k=5)
letters_and_digits.extend(choices(digits, k=5))
incorect_login = ''.join(letters_and_digits)
try:
    if check(incorect_login):
        print("checked successfully")
except ValueError as e:
    print(str(e) == f"incorrect login '{incorect_login}'")