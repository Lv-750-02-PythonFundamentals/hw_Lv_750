"""password checker"""

import re
patern = r'[A-Za-z0-9$#@]{6,16}'
parametrs_of_pasword = """The password must contain at least one character from the list:a-z, A-Z, @#$, 0-9.
Password length from 6 to 16 characters.
"""
while True:
    print(parametrs_of_pasword)
    password = input('Input password : ')
    if re.match(patern, password):
        print('Very nice password. Much secure')
        break
    else:
        print('Not a valid password')