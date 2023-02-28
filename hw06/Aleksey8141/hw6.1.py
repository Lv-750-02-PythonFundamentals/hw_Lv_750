'''Create a list of integers that are entered from the terminal and
determine the maximum and minimum number among them.'''

l_num = input("Enter a number: ").split()
l_num = [int(num) for num in l_num]
max_num = max(l_num)
min_num = min(l_num)

print("Max number:", max_num)
print("Min number:", min_num)