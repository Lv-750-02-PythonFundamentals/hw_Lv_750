import hw08_03_01

while True:
    figure = input("Enter the figure (Rectangle, triangle, circle): ")

    if figure.lower() == "triangle":
        a = int(input("Enter base of triangle: "))
        h = int(input("Enter height of triangle: "))
        print("Area of triangle:", hw08_03_01.triangle_area(a, h))
        break
    elif figure.lower() == "rectangle":
        a = int(input("Enter length of rectangle: "))
        b = int(input("Enter width of rectangle: "))
        print("Area of rectangle:", hw08_03_01.rectangle_area(a, b))
        break
    elif figure.lower() == "circle":
        r = float(input("Enter radius of circle: "))
        print("Area of circle:", hw08_03_01.circle_area(r))
        break
    else:
        print("Invalid figure. Try again.")

        