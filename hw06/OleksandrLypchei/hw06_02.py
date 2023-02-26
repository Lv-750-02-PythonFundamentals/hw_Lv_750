login = ''

while login != 'First':
    login = input('Enter login: ')
    if login == 'First':
        print('Greetings, Mr. First!')
    else:
        print('Login error! Login is not valid.')
