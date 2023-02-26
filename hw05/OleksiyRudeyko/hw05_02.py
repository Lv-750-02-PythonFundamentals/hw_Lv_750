num = int(input("Enter number: "))
fib1 = 0
fib2 = 1

print(fib1)
print(fib2)

while fib2 < num:
    fib3 = fib1 + fib2

    if fib3 <= num:
        print(fib3)

    fib1 = fib2
    fib2 = fib3
