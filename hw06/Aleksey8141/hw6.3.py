'''Write a script that checks the login that the user enters.
If the login is "First", then greet the users. If the login is
different, send an error message.
(need to use loop while)'''

login = input('Enter your login: ')

while login == 'First':
    print('Your login is confirmed')
    break
else:
    print('Wrong login, please try again')

