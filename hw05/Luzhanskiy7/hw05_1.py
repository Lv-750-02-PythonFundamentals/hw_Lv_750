import random

my_list = []
my_list_float = []
for i in range(10):
    my_list.append(random.randrange(1, 100))
for j in my_list:
    my_list_float.append(float(j))
print(my_list)
print(my_list_float)