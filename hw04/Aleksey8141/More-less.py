'''Write a script, which of the two entered
numbers will determine which of them is
more and which is less. Take into account
the case of equality of numbers'''

a = int(input())
b = int(input())

if a>b:
    print('a is bigger than b by', a - b)
elif a<b:
    print('b is bigger than a by', b - a)
else:
    print('a is equal to b')
