# Print all even numbers less than 100
# (write two variants of the code:
# one using the while loop,
# and
# the other using the for loop).

i = 1

while i < 100:
    if i%2==0:
        print(i)
    i+=1


for i in range(2,100):
    if i%2==0:
        print(i)

for i in range(2,100,2):
    print(i)