import random
int_list = []
for i in range(10):
    int_list += [random.randint(1, 19)]
print(int_list)
print([float(x) for x in int_list])

