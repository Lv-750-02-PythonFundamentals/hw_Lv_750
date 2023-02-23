list_of_elements = ["e", 6, 5.4, 543, (4, 4.5), 2341, False, 3]

for i in range(len(list_of_elements)):
    if type(list_of_elements[i]) is int:
        list_of_elements[i] = float(list_of_elements[i])
    else:
        continue
else:
    print(list_of_elements)
