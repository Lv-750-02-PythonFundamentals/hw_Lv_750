class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        pass

class Rectangle(Polygon):
    def __init__(self, lenght, width):
        super().__init__([lenght, width])

    def area(self):
        return self.sides[0] * self.sides[1]
    
rect = Rectangle(4, 6)
print(f"Rectangle area: {rect.area()}")
