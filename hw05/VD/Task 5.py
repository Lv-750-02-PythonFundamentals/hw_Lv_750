# Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

number = int(input("Please enter your number: "))
num = 1
previos_num = 0
next_num = 0
for i in range(number):
    print(previos_num)
    next_num = previos_num + num
    previos_num = num
    num = next_num
    
# pythonic way
number = int(input("Please enter your number: "))
num = 0
next_num = 1
for i in range(number):
    print(num)
    num, next_num = next_num, num + next_num
   