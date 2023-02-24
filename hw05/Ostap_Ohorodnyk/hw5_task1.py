number_for_list = int(input("enter a number for the length of the list: "))
my_list = [*range(1, number_for_list+1)]
float_list = []

for number in my_list:
    float_list.append(float(number))

print("List of int number ", my_list)
print("List of float number ", float_list)