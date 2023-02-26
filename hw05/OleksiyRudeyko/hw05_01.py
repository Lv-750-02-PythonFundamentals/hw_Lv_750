inputs = input("Enter your numbers: ").split(", ")
list_of_ints = []

for x in inputs:
    if x.isdigit() == False:
        
        print("Error... You should enter numbers.")
        break

    else:
        list_of_ints.append(float(x))

    print(list_of_ints)
