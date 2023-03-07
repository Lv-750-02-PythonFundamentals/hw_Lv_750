# Print all even numbers less than 100
# (write two variants of the code:
# one using the while loop,
# and
# the other using the for loop).

## while solution
i = 0
while i < 100:
    i += 2
    if i == 100:
        break
    else:
        print(i)

## for solution
for i in range(2, 100, 2):
    print(i)