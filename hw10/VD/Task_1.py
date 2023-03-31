"""Create a polygon class and a rectangle class
that inherits from the polygon class and finds the square
of rectangle
"""

class Polygon:
    def __init__(self, sides = 0):
        self.sides = sides
    # def __str__(self) -> str:
    #     return f"sides: {self.sides}"

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(4)
    def __str__(self) -> str:
        return f"sides: {self.sides}"

a = Polygon()
b = Rectangle()

print(a.sides)
print(b.sides)

print(a)
print(b)