inputs = input("Enter your numbers: ").split(", ")
list_of_ints = []

for x in inputs:
    if x.isdigit() == False:
        continue
    list_of_ints.append(float(x))

if list_of_ints != []:
    print(list_of_ints)
else:
    print("You should enter at least one number!")
