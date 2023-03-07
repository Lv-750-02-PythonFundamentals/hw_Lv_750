login = 'First'
while True:
    user = input('Enter login:')
    if user != login:
        print('Error, wrong login!!!')
    else:
        print(f'Hello{login}!!!')
        break
