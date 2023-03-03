def area():
    """Program that calculates the area of a rectangle,
       triangle and circle"""
    def area_of_triangle():
        message_triangle = input("Enter three numbers - the sides of the triangle. "
                                      "(Enter numbers using a space): ").split()
        s = (int(message_triangle[0]) + int(message_triangle[1]) + int(message_triangle[2])) / 2
        print("Area of a triangle = ", s)
        return s

    def area_of_square():
        message_square = input("Enter two numbers - the sides of the square. "
                               "(enter numbers using a space) : ").split()
        s = int(message_square[0]) * int(message_square[1])
        print("Area of a square = ", s)
        return s

    def area_of_circle():
        message_circle = int(input("Enter the radius of the circle : "))
        s = 3.14 * (message_circle**2)
        print("Area of a circle = ", s)


    message_area = input("Hello. Choose one of the options:""\n"
                        "1. Area of a triangle;""\n"
                        "2. Square area;""\n"
                        "3. Area of a circle. : ")

    while int(message_area) > 3 :
        print("Please enter a number from the menu")
        message_area = input("Hello. Choose one of the options:""\n"
                             "1. Area ofa triangle;""\n"
                             "2. Square area;""\n"
                             "3. Area of a circle.""\n")

    if int(message_area) == 1:
        area_of_triangle()
    elif int(message_area) == 2:
        area_of_square()
    elif int(message_area) == 3:
        area_of_circle()


area()
print(area.__doc__)