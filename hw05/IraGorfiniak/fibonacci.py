number = int(input("Enter number for Fibonacci sequence: \n"))

n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if number <= 0:
    print("Please enter a positive integer")
elif number == 1:
    print("Fibonacci sequence", number,":")
    print(n1)
else:
    print("Fibonacci sequence", number, ":")
    while count < number:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
