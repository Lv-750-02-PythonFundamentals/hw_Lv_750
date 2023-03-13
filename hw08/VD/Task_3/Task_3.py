"""Module with functions"""

from math import sqrt, pi, pow

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
    return (pi * pow(r, 2))

