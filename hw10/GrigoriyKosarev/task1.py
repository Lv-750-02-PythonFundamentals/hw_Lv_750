

class Polygon():
    """Polygon class"""
    pass


class Rectangle(Polygon):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(2.0, 3.0)
print(rectangle.area())
