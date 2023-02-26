# Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

number = int(input('Input number:'))

previous_val = 0
next_val = 1

for i in range(0, number):
    if i <= 1:
        next_val = i
    else:
        previous_val, next_val = next_val, previous_val + next_val
    print(next_val)
    