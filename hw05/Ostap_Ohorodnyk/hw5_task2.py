number = int(input("enter a number of the length of the list of Fibonacci numbers:  "))
n1, n2 = 0, 1
count = 0
list_of_fibonacci_numbers = []
while number <= 0:
   print("Please enter a positive integer")
   number = int(input("enter a number of the length of the list of Fibonacci numbers: "))
if number == 1:
   print("Fibonacci sequence upto",number,"=", n1)
else:
   print("Fibonacci sequence:")
   while count < number:
       list_of_fibonacci_numbers.append(str(n1))
       step = n1 + n2
       n1 = n2
       n2 = step
       count += 1
print(F'A list of Fibonacci numbers of length {number} numbers = {", ".join(list_of_fibonacci_numbers)}')