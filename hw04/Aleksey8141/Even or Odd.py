'''
Write a script that will check whether
the entered number is even or odd and
display the appropriate message.
'''

a = int(input())

if a%2==0:
    print('a is an even number')
else:
    if a%2!=0:
        print('a is an odd number')
