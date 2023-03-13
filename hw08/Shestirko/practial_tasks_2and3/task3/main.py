from geometry import rectangle_area, triangle_area, circle_area

while True:
    print("Choose a shape to calculate the area of:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Quit")
    
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        a = float(input("Enter the length of the rectangle: "))
        b = float(input("Enter the width of the rectangle: "))
        print("The area of the rectangle is:", rectangle_area(a, b))
    elif choice == 2:
        h = float(input("Enter the height of the triangle: "))
        a = float(input("Enter the base length of the triangle: "))
        print("The area of the triangle is:", triangle_area(h, a))
    elif choice == 3:
        r = float(input("Enter the radius of the circle: "))
        print("The area of the circle is:", circle_area(r))
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")