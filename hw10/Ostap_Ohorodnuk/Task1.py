""""A polygon class and a rectangle class"""


class Polygon:
    """polygon class"""
    pass


class Rectangle(Polygon):
    """rectangle class"""
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b

    def square(self):
        self.a = int(input("enter side a: "))
        self.b = int(input("enter side b: "))
        return self.a * self.b

square_of_rectangle = Rectangle()
print(square_of_rectangle.square())