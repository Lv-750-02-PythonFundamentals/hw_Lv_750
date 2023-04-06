"""Rewrite the following code through using the map function. The
function takes a list of real names and replaces them with the
appropriate hash combinations using the hashing method.
names = ['Sam', 'Don', 'Daniel']
for i in range(len(names)):
names[i] = hash(names[i])
print(names)
# => [6306819796133686941, 8135353348168144921, -1228887169324443034]
"""

names = ['Sam', 'Don', 'Daniel']
hash_names = list(map(lambda name: hash(name), names))
print(hash_names)



"""All these numbers in the list have a string data type, for example
['1', '2', '3', '4', '5', '7'], convert this list to a list, all numbers of
which have the data type integer :
1) using the append method
2) using the map method
"""

str_lst = ['1', '2', '3', '4', '5', '7']

# 1
int_lst = []
for num in str_lst:
    int_lst.append(int(num))
print(int_lst)

# 2
int_lst = list(map(lambda num: int(num), str_lst))
print(int_lst)



"""Convert list containing miles to list containing kilometers (1 mile
= 1.6 kilometers)
a) using the map and some function
b) using the map and lambda function
"""

# a
miles = [100, 123, 1, 52, 68, 0]

def mls_to_kms(arg):
    km = 1.6 * arg
    return km

kms = list(map(mls_to_kms, miles))
print(kms)

# b
kms = list(map(lambda mls: mls * 1.6, miles))
print(kms)
