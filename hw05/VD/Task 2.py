# Print all odd numbers less than 100.
# (write two versions of the code:
# one using the continue operator,
# and
# the other without this operator).

## while solution
i = 1
while i < 100:
    print(i)
    i += 2

## for solution
for i in range(1, 100, 2):
    print(i)