# Create a list of integers that are entered from the terminal and
# determine the maximum and minimum number among them.

x = int(input("How many numbers do you want to enter? "))
my_list = []
count = 1
while count <= x:
    count += 1
    my_list.append(int(input("Please enter your number: ")))
print(my_list, "\nminimum number is:", min(my_list), "\nmaximum number is:", max(my_list))

# ver2
print("\n")
my_list = [int(input()), int(input()), int(input())]
print(my_list, "\nminimum number is:", min(my_list), "\nmaximum number is:", max(my_list))

# ver3

numbers = input("\nPlease enter your numbers and press Enter: ")
numbers = numbers.replace(" ", "") if " " in numbers else numbers
my_list = [i for i in numbers]
print(my_list, "\nminimum number is:", min(my_list), "\nmaximum number is:", max(my_list))

# ver4

numbers = input("\nPlease enter your numbers and press Enter: ")
numbers = numbers.replace(" ", "") if " " in numbers else numbers
my_list = list(numbers)
print("\n", my_list, "\nminimum number is:", min(my_list), "\nmaximum number is:", max(my_list))