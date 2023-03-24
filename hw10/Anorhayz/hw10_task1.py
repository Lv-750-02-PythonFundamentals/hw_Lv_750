class Polygon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def square(self):
        return self.x * self.y


class Rectangle(Polygon):
    pass


some_polygon = Rectangle(8, 5)
print(some_polygon.square())
