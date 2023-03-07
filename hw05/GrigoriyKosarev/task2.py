import math

"""
Print Fibonacci numbers up to the entered number n,
using cycles.
(Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)
"""
def fibonacci_numbers(n):
    if n < 0:
        return "Value is less 0"
    if n == 0:
        return 0
    if n == 1:
        return 1

    fibonacci = [0, 1, 1]
    i = 2
    while i <= n-1:
        fibonacci.append(fibonacci[len(fibonacci)-1] + fibonacci[len(fibonacci)-2])
        i += 1

    return fibonacci

print(fibonacci_numbers(10))

