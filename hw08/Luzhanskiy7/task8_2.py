import re

while True:
    password = input('Enter password: ')
    a_z = re.findall('[a-z]', password)
    a_z_big = re.findall('[A-Z]', password)
    numbers = re.findall('[0-9]', password)
    special = re.findall('[@#$]', password)
    if len(a_z) > 0 and len(a_z_big) > 0 and len(numbers) > 0 and len(special) > 0 and 6 <= len(password) <= 16:
        print('Good password')
        break
    else:
        print('Your password must contain one of these characters (a-z,A-Z,0-9,@#$)\nAnd must be min 6 max 16 symbols')


