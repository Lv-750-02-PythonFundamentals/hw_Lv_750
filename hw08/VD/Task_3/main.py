# Start programm
# User making choise what operation to do

from Task_3 import area_tri, area_rec, area_cir


flag = True
while flag:
    print("Please choose what operation you would like to proceed")
    print("Enter:")
    choise = ""
    while choise != "T" and choise != "R" and choise != "C":
        print("---'T' for Triangle square calculation")
        print("---'R' for Rectangle square calculation")
        print("---'C' for Circle square calculation")
        print("---'Q' to Quit")
        choise = input("Your choise: ")
        if choise == "Q":
            flag = False
            break

        # Triangle option
        if choise == "T":
            func = area_tri
            
        # Rectangle choise
        elif choise == "R":
            func = area_rec
            
        # Circle choise
        elif choise == "C":
            func = area_cir

        # Result
        print("\nArea is", round(func(), 1), end="\n\n")