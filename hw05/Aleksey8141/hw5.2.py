'''Print Fibonacci numbers up to the entered number n,
using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)'''

n = int(input("Enter a number: "))
a, b = 0, 1
while a <= n:
    print(a, end=' ')
    a, b = b, a+b