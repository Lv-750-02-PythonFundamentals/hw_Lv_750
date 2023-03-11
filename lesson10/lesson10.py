#
#
# class MyClass:
#     cm = []
#     ci = 25
#     def __init__(self):
#         print("test",id(self), self.__dict__)
#         self.im = []
#         self.ii = 25
#         print("test",id(self), self.__dict__)
#
#     def __eq__(self, other):
#         # return id(self) == id(other)
#         return self.ii == other.ii
#
# a1 = MyClass()
# a2 = MyClass()
# print(type(a1), id(a1))
# print(type(a2), id(a2))
# a3 = a1
# print(a1 == a2)
# print(a1 == a3)
# print(a1 is a3)
# # print(a1.cm, a1.ci, a1.im, a1.ii)
# # print(a2.cm, a2.ci, a2.im, a2.ii)
# # a1.im.append(22)
# # a2.im.append("atest")
# # a2.ii = 12
# # a2.cm.append("88")
# #
# # print(a1.cm, a1.ci, a1.im, a1.ii)
# # print(a2.cm, a2.ci, a2.im, a2.ii)
#
# # print(dir(a1))
# # print(id(a1), a1.__dict__)
# # print(MyClass.__dict__)

class Point(object):
    # instanc = None
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.instanc is None:
    #         cls.instanc = super(Point, cls).__new__(Point)
    #     return cls.instanc

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print(self):
        print(f"x:{self.x} y:{self.y}")

    def __str__(self):
        return f"x={self.x}  y={self.y}"

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance(self, point):
        return ((point.x - self.x) ** 2 + (point.y - self.y) ** 2) ** 0.5

    def __add__(self, other):
        point = Point()
        if type(other) is Point:
            point.x = self.x + other.x
            point.y = self.y + other.y
        elif type(other) is int:
            point.x = self.x + other
            point.y = self.y + other
        else:
            return None
        return point


class Triangle:
    def __init__(self, p1, p2, p3):
        print(p1, p2, p3)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perymeter(self):
        return self.p1.distance(self.p2) + self.p2.distance(self.p3) + self.p3.distance(self.p1)


class Triangle2:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def perymeter(self):
        return (((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5 +
                ((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2) ** 0.5 +
                ((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2) ** 0.5)


#
# # Point(99, 99)
# p1 = Point(12, 22)
# p2 = Point(-7, 33)
# # p3 = Point(-7, 33)
# # p4 = Point(-7, 33)
# # p5 = Point(-7, 33)
# # print(p1, p2, p3,p4,p5)
# print(p1)
#
# p1.print()
# p2.print()
# print(p1.__dict__)
#
#
# def my_f(p, v):
#     p.x += v
#     p.y = p.y + v
#
#
# my_f(p1, 100)
# p1.print()
#
# Point.f = my_f
# p2.f(10000)
# p2.print()
# Point.print(p1)
points = []
for i in range(3):
    p = Point()
    p.x = int(input("x: "))
    p.y = int(input("y: "))
    points.append(p)
print(points)
t = Triangle(*points)
print(t.perymeter())
print(points[0] + points[1])
print(points[0] + 3)
print(points[0] + "3")
# p1 = Point(0, 0)
# p2 = Point(0, 1)
# p3 = Point(1, 0)
# t = Triangle(p1, p2, p3)
# print(t.perymeter())
# t2 = Triangle2(0, 0, 0, 1, 1, 0)
# print(t2.perymeter())
