# Task1. Create a polygon class and a rectangle class
# that inherits from the polygon class and finds the square
# of rectangle.

class Polygon:
    pass

class Rectangle(Polygon):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y
    
rectangle = Rectangle(2, 4)
print(rectangle.square())