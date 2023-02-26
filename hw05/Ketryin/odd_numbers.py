# Print all odd numbers less than 100.
# (write two versions of the code:
# one using the continue operator,
# and
# the other without this operator).

i = 1

while i < 100:
    if i%2==1:
        print(i)
        i+=1
    else:
        i+=1
        continue

for i in range(1,100):
    if i%2==1:
        print(i)

for i in range(1,100,2):
    print(i)