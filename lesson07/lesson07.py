# list1 = ['xyz', 'zara', 'PYnative',  'aYnative']
# print(max(list1))
# print(min(list1))
#
# for word in list1:
#     sum = 0
#     for i in word:
#         sum += ord(i)
#     print(word, sum)
# def my_func():
#     a = 1
#     return a
# print(my_func())
#
# def my_func():
#     a = 1
# print(my_func())
#
#
# def my_func(a, b):
#     """
#     todo
#     some text
#
#     :param a: int
#     :param b: int
#     :return: int a*b
#     """
#     return a*b
#
# print(my_func.__doc__)
# # sum()
# # my_func()
# help(sum)
# help(my_func)
#
# def my_func(a, b):
#     """
#     todo
#     some text
#
#     :param a: int
#     :param b: int
#     :return: int a*b
#     """
#     return

# def my_function():
#     print(1)
#     print(2)
#     return
#     print(3)
#     print(4)
# my_function()
#
# def greet(name):
#     """This function greets to
#     the person passed in as
#     parameter"""
#     print("Hello, " + name + ". Good morning!")
#
# print(greet)
# greet("Liubomyr")
# greet("Anna")
#
# a = [1,2,3,4]
# b = a
# c = greet
# c("Vasyl")
# greet("Vasyl2")

# def my_func(arg_1, arg_2):
#     pass
# # my_func()
# # my_func(1)
# my_func(1,2)
# my_func(1,2,3)

# def print_info(name, age=18):
#     print("Name: ", name)
#     print("Age: ", age)

#
# # print_info()
# result = print_info("Liubomyr")
# print(result)
# print_info("Liubomyr")
# print_info("Liubomyr", 36)
#
# def my_func(a,  c, b=10):
#     pass
# def print_info(name, age=18) -> list:
#     print("Name: ", name)
#     print("Age: ", age)
#
#
# print_info(12, 12)

# def my_func(a=1, b=[]):
#     print(a, b)
# my_func()
# my_func(12, [1,2,3])
# my_func()
# def my_func(a=1, b=[]):
#     b.append(a)
#     print(a, b)
# my_func()
# my_func()
# my_func()
# my_func(3, [99])
# my_func(99)
# my_func()
# my_func()

# def my_func(a=1, b=(1, [1, 3])):
#     b[1].append(a)
#     print(a, b)
# my_func()
# my_func()
# my_func()
# my_func(3, [99, [88]])
# my_func(99)
# my_func()
# my_func()
#
# def my_func(a=1, b=None):
#     if b is None:
#         b = []
#     b.append(a)
#     print(a, b)
#
#
# my_func()
# my_func()
# my_func()
# my_func(3, [99])
# my_func(99)
# my_func()
# my_func()

# def my_func(c, a=1, b=None):
#     print(f"{c=} {a=} {b=}")
#
#
# my_func(b=[9, 8, 7, 6], c="test", a=99)
# my_func([9, 8, 7, 6], "test", 99)
#
#
# print([], end="12")
# def my_f(*args, **kwargs):
#     print(f"{args=} {kwargs=}")
#
#
# my_f()
# my_f(1, 1, 2, 3, 4)
# my_f(k=1, w=33, m=[1, 3])
# my_f(1, 1, 2, 3, 4, k=1, w=33, m=[1, 3])

# def my_f(a, b, c, *args, d=0, e=0, g=0, **kwargs):
#     print(f"{a=} {b=} {c=} {args=} {d=} {e=} {g=} {kwargs=}")
#
#
# my_f(1, 2, 3, 4, 5, e=1, g=3, x=3)
# def my_f(a, b, c,  d=0, e=0, g=0, **kwargs):
#     print(f"{a=} {b=} {c=} {d=} {e=} {g=} {kwargs=}")
#
#
# # my_f(1, 2, 3, 4, 5, e=1, g=3, x=3)
# my_f(1, 2, 3, 4, 5, g=3, x=3)


# def dec(func):
#     def wrap():
#         print(func)
#         return func()
#     return wrap
#
# @dec
# def my_f1():
#     print("f1")
# @dec
# def my_f2():
#     print("f2")
# @dec
# def my_f3():
#     print("f3")
#
# my_f3()
# my_f2()
# my_f1()
# my_f1()
# my_f1()
# my_f1()
# my_f1()
# def f1(a, b):
#     return a + b
#
#
# def f2(a, b):
#     return a * b
#     # pass
#
#
# if (f1(1, 2) > f2(2, 3)):
#     print("true")
# else:
#     print("false")

#
# print(dir())
#
#
# def my_f():
#     print("\t", dir())
#     a = [112]
#     b = [112]
#     print("\t",id(a))
#     print("\t",id(b))
#     print("\t", dir())
#     return a
# # print(a)
#
# print(dir())
# a1 = my_f()
# a2 = my_f()
# a3 = my_f()
# print(id(a1))
# print(id(a2))
# print(id(a3))
# print(dir())
# print(a)


# a = 10
#
# def my_func():
#     print(a)
#
# my_func()
# my_func()
# my_func()
#
# a = 10
#
# def my_func():
#     print(a)
#     a = 20
#     print(a)

# my_func()
# my_func()
# my_func()
# print(a)

#
# a = [10]
#
# def my_func():
#     print(a)
#     a.append(20)
#
# my_func()
# my_func()
# my_func()
# print(a)

#
# a = 10
#
# def my_func():
#     global a
#     print(a)
#     a = 20
#
# my_func()
# # print(a)
# def f():
#     x = 10
#     def f1():
#         nonlocal x
#         def f2():
#             nonlocal x

# 5! 1*2*3*4*5
# def fac_1(n):
#     print(n)
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print(fac_1(5))
# print(fac_1(8))
# def fac_2(n):
#     print(n)
#     if n <= 1:
#         return 1
#     return n * fac_2(n-1)
#
# print(fac_2(5))
# print(fac_2(8))
# 5 * fac_2(4) ->5*(4*fac_2(3)) ->5*(4*(3*fac_2(2)))  ->5*(4*(3*(2*fac_2(1)))) ->5*(4*(3*(2*1)))

# def fac_2(n):
#     print(n)
#     return fac_2(n-1)
# import sys
# sys.setrecursionlimit(1500)
# fac_2(10000)
# print(2**45)
#
# my_f = lambda a, b: a+b
# print("test")
# print(my_f(1,2))
# print(my_f(1,2))
# print(my_f(1,2))

l = [1, 2, 3, 4, "aa", 12, 2]
l.sort(key=lambda a: str(a))
l.sort(key=lambda a: str(a))
print(l)
l = [1, 2, 3, 4, "aa", 12, 2]
def to_str(a):
    return str(a)
l.sort(key=to_str)
print(l)