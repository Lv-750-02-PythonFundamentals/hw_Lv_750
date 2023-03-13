"""Write a program that calculates the area of a rectangle,
triangle and circle
(write three functions to calculate the area, and call them in the
main program depending on the user's choice)
"""
from math import sqrt

def area_tri():
    """Fuction accepts triangle's sides length and triagle's hight and returns it's area"""
    print("\nThere are 2 available ways you may find the area of triangle:")
    print("---1st - you need to know triangle's base nad its hight")
    print("---2nd - you need to know all 3 sides of the triangle")
    choise_2 = input("Please type your way '1' or '2': ")
    if choise_2 == "1":
        a = int(input("\nPlease enter length of the base of triangle: "))
        h = int(input("Please enter hight of triangle: "))
        return a * h / 2
    elif choise_2 == "2":
        a = int(input("\nPlease enter length of the 1st side of triangle: "))
        b = int(input("Please enter length of the 2nd side of triangle: "))
        c = int(input("Please enter length of the 3rd side of triangle: "))
        s = (a + b + c) / 2
        return sqrt(s * (s - a) * (s - b) * (s - c))  # math error possible due to not correct values enter
    else:
        print("\nOoops, it looks like you did not enter needed data properly, please try again...")

def area_rec():
    """Function accepts rectangle sides value and returns its area"""
    print("\nPlease enter length of two NOT OPPOSITE sides")
    a, b = int(input("side a = ")), int(input("side b = "))
    return a * b

def area_cir():
    """Function accepts circle radius and returns its area"""
    print("\nPlease enter RADIUS of the circle")
    r = int(input("RADIUS = "))
    return (3.14 * r ** 2)

# Start programm
# User making choise what operation to do
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