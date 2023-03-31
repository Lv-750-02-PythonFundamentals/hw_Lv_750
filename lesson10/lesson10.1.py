# class Point:
#     def __init__(self, x=0, y=0):
#         print("Point")
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"({self.x}, {self.y})"
#
#     def __str__(self):
#         return f"x:{self.x} y:{self.y}"
#
#
# points = [Point(), Point(1), Point(y=1)]
# print(points)
#
#
# class Point3D(Point):
#     def __init__(self, x=0, y=0, z=0):
#         print("Point3D")
#         super().__init__(x, y)
#         # self.x = x
#         # self.y = y
#         self.z = z
#
#     def __repr__(self):
#         return f"({self.x}, {self.y}, {self.z})"
#
#     def __str__(self):
#         return f"x:{self.x} y:{self.y} z:{self.z}"
#
#
# points = [Point3D(), Point3D(1), Point3D(y=1)]
# print(points)
# print(points[0])
#
#
# class A:
#     def print_a(self):
#         print("A")
#
#
# class B(A):
#     def print_b(self):
#         print("B")
#
#     def print(self):
#         print("B", self.__class__)
#
#
# class C(A):
#     def print_c(self):
#         print("C")
#
#     def print(self):
#         print("print")
#
#
# class D(B, C):
#     pass
#
#
# d = D()
# d.print_a()
# d.print_b()
# d.print_c()
# d.print()
#
#
# class A: pass
#
#
# class B(A): pass
#
#
# class C(B): pass
#
#
# class D(B): pass
#
#
# # class E(A): pass
#
#
# class F(E, D): pass
#
#
# class G(C): pass
#
#
# class T(G, F): pass
#
#
# class M(T, E): pass
#
#
# m = M()
# print(M.__mro__)


# class Temp:
#     def inst(self):
#         print(self)
#
#     @classmethod
#     def clas(cls):
#         print(cls)
#
#     @staticmethod
#     def stat():
#         print("statatic")
#
#
# t = Temp()
# t.inst()
# t.clas()
# # Temp.inst() #error
# Temp.clas()
#
#
# t.stat()
# Temp.stat()
#
#
# class E(object):
#     def __init__(self, a, b, c):
#         self.public = a
#         self._protected = b
#         self.__private = c
#
#     def print_private(self):
#         print(self.__private)
#
#     def __set_private(self, pr):
#         self.__private = pr
#
#
# x = E(11, 13, 17)
# print(x._E__private)
# x.print_private()
# x._E__set_private(99)
# print(x._E__private)
# x.print_private()

#
# class P:
#     def __init__(self, x):
#         # self.__set_x(x)
#         self.__x = x
#
#     def __get_x(self):
#         print("__get_x")
#         return self.__x
#
#     def __set_x(self, x):
#         print("__set_x")
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
#
#     def __repr__(self):
#         return f"{self.__x}"
#
#     x = property(__get_x, __set_x)
#
# p = P(1)
# p.x
# p.x = 10
#
#
# class P:
#     def __init__(self,x):
#         self.__x = x
#     @property
#     def x1(self):
#         print("new__get_x")
#         return self.__x
#     @x1.setter
#     def x1(self, x):
#         print("new x.setter")
#         if x < 0:
#             self.__x = 0
#         elif x > 1000:
#             self.__x = 1000
#         else:
#             self.__x = x
# p = P(1)
# p.x1
# p.x1 = 10


class A:
    def print(self):
        print(self)

    def print(self, st):
        print(st, self)
a = A()
a.print("dhsbv")

class Point():
    def __init__(self, x=0, y=0):
        print("Point")
        self.x = int(x)
        self.y = int(y)

Point()
Point(12, 12)
Point("12"," 12")
