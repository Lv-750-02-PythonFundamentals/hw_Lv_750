class Polygon:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.sides = [0 for _ in range(num_sides)]

    def set_sides(self, sides):
        if len(sides) == self.num_sides:
            self.sides = sides
        else:
            raise ValueError(f"Number of sides provided ({len(sides)})"
                             f" does not match the number of sides of the polygon ({self.num_sides}).")

class Rectangle(Polygon):
    def __init__(self):
        super().__init__(num_sides=4)

    def area(self):
        if self.sides[0] == 0 or self.sides[1] == 0:
            raise ValueError("Sides of the rectangle must be set before calculating the area.")
        return self.sides[0] * self.sides[1]


rectangle = Rectangle()
rectangle.set_sides([5, 10, 5, 10])
print(rectangle.area())