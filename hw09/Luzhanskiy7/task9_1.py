from random import randint
number = randint(1, 100)

for i in range(1, 11):
    atempt = int(input('Guess the number from 1 to 100: '))
    if atempt == number:
        print('Yes, you guessed it', number)
        break
    elif atempt > number:
        print(f'incorrect, your number is greater, {10 - i} attempt left')
    elif atempt < number:
        print(f'incorrect, your number is less, {10 - i} attempt left')
print('Sorry, the attempts are over')