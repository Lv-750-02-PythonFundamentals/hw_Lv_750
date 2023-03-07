def find_largest_number(num1, num2):
    """The  function finds the largest number"""

    return f"The largest numer is {num1}" if num1 > num2 else f"The largest numer is {num2}" if num2 > num1 \
        else "The numbers are equal"


def calculate_characters(string):
    """The  function calculates the number of characters included in the given string"""

    return {x: string.count(x) for x in string}


def calculate_rectangle_area(a, b):
    """The  function calculates the area of rectangle"""
    return a*b


def calculate_triangle_area(a, h):
    """The  function calculates the area of triangle"""
    return 0.5*a*h


def calculate_circle_area(r):
    """The  function calculates the area of circle"""
    return 3.14*r**2


def main():
    """Main controller"""
    user_choice = input("Enter the area of which shape you want to calculate(rectangle, triangle, circle): ")
    if user_choice.strip().lower() == "rectangle":
        try:
            a, b = map(int, input("Enter the lengths of the rectangle sides: ").split())
            area = calculate_rectangle_area(a, b)
            print(f"The area of rectangle is {area}")
        except:
            print("The entered data is incorrect")
    elif user_choice.strip().lower() == "triangle":
        try:
            a, h = map(int, input("Enter the length of the side and height of the triangle: ").split())
            area = calculate_triangle_area(a, h)
            print(f"The area of triangle is {area}")
        except:
            print("The entered data is incorrect")
    elif user_choice.strip().lower() == "circle":
        try:
            r = int(input("Enter the length of the circle radius: "))
            area = calculate_circle_area(r)
            print(f"The area of circle is {area}")
        except:
            print("The entered data is incorrect")
    else:
        print("The entered data is incorrect")


if __name__ == "__main__":
    print(find_largest_number(7, 1))
    print(calculate_characters("Hello world!"))
    main()
