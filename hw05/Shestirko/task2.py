n = int(input("Enter a number: "))
fib1, fib2 = 0, 1

print(fib1)
print(fib2)

while fib2 <= n:
    fib3 = fib1 + fib2
    if fib3 <= n:
        print(fib3)
    
    fib1, fib2 = fib2, fib3
