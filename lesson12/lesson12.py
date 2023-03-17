# vec1 = [3, 10, 2]
# vec2 = [-20, 5, 1]
#
# print(list(zip(vec1, vec2)))
# print(list(zip(vec1, vec2 + vec2)))
# print(list(zip(vec1, vec2 + vec2, [1, 2])))
#
# winning_lottery_numbers = [0, 4, 3, 2, 3, 1]
#
#
# def s(e):
#     return e ** 2
#
#
# print(list(map(s, winning_lottery_numbers)))
# print(list(map(lambda e: e ** 3, winning_lottery_numbers)))

#
# import random
# names = ['Sam', 'Don', 'Sid']
# code_names = ['Iron', 'Batman', 'Capitan']
# for i in range(len(names)):
#     names[i] += random.choice(code_names)
# print(names)
#
# print(list(map(lambda n: f"{n} {random.choice(code_names)}", names)))
# print(list(map(lambda n: f"{n} {random.choice(code_names)}", names)))
#
#
# def isPos(number):
#     return number > 0
#
# a = [-1,2,-3,4,-5,6,-7,8,-9,10]
# print(list(filter(isPos, a)))
# print(list(filter(lambda e: not isPos(e), a)))
#
#
# l = [-1,2,-3,4,-5,6,-7,8,-9,10]
#
# def f(a , b):
#     r = a + b
#     print(f"{a}+{b}={r}")
#     return r
# from functools import reduce
# print(reduce(f, l))
# print(reduce(f, l, 100))

# name_str = "Liubov"
# custom_iterator = iter(name_str)
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# print(next(custom_iterator))
# # print(next(custom_iterator)) #error StopIteration
#
# class MyNumbers:
#     def __iter__(self):
#         print("__iter__")
#         self.a = 1
#         return self
#
#     def __next__(self):
#         print("__next__")
#         x = self.a
#         self.a += 1
#         return x
#
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

#
# class MyList:
#     def __init__(self, *args):
#         self.elements = args
#
#     def __iter__(self):
#         # print("__iter__")
#         self.iter_index = 1
#         return self
#
#     def __next__(self):
#         # print("__next__")
#         if self.iter_index >= len(self.elements):
#             raise StopIteration
#         x = self.elements[self.iter_index]
#         self.iter_index += 1
#         return x
#
#     def __str__(self):
#         return f"<{', '.join(map(lambda e: e.__repr__(), self.elements))}>"
#
#     def __repr__(self):
#         return f"<{', '.join(map(lambda e: e.__repr__(), self.elements))}>"
#
#
# my_list = MyList(1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)
# # my_list = iter(my_list)
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# # print(next(my_list))
# for i in my_list:
#     print(i)
# for i in my_list:
#     print(i)
# print(my_list)
#
# a = [MyList(1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1)]
# print(a)


# g = (x*x for x in range(1, 4))
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# def my_namge(n):
#     print("= 1")
#     yield 1
#     print("= 2")
#     yield 2
#     print("= 3")
#     yield 3
#     print("= 4")
# def my_namge(n):
#     i = 0
#     while True:
#         yield i
#         i += 1
#         if i >= n:
#             break
#
# a =  my_namge(5)
# print(a)
# print("-----------")
# print(next(a))
# print("-----------")
# print(next(a))
# print("-----------")
# print(next(a))
# print("-----------")
# print(next(a))
# print("-----------")
#
# for i in my_namge(5):
#     print(i)
#
#
# l = ["*"*i for i in range(1000)]
# # print(l)
# print(l.__sizeof__())
# l = ("*"*i for i in range(1000))
# print(l.__sizeof__())
#
# l = ["*"*i for i in range(10000)]
# # print(l)
# print(l.__sizeof__())
# l = ("*"*i for i in range(10000))
# print(l.__sizeof__())

#
# def dec(func):
#     print(f"create decorator {func.__name__} {id(func)}")
#
#     def wraper(*args_w, **kwargs_w):
#         print(f"run decorator {args_w} {kwargs_w}")
#         result = func(*args_w, **kwargs_w)
#         print("end run")
#         return result
#
#     print(f"end create {id(wraper)}")
#     return wraper
#
#
# @dec
# def my_sum(a, b):
#     return a + b
#
#
# @dec
# def my_sorted(*args, **kwargs):
#     return sorted(*args, **kwargs)
#
#
# print(id(my_sum))
# print(id(my_sorted))
# print(my_sum(1, 7))
# print(my_sum(3, 3))
# print(my_sum(12, 4))
# print(my_sorted([1, 2, 3, "4"], key=lambda x: int(x)))
# print(sorted([1, 2, 3, "4"], key=lambda x: int(x)))
#

def decorator_factory(sap="*", *args, **kwargs):
    print("init decorator")
    def decorator(func):
        print("create decorator")
        def wraper(*args_w, **kwargs_w):
            print(sap * 10)
            print(f"run {func.__name__} with {args_w} {kwargs_w}")
            result = func(*args_w, **kwargs_w)
            print(f"result={result}")
            return result

        print("end create")
        return wraper

    print("end init")
    return decorator


@decorator_factory()
def my_sum(a, b):
    return a + b


@decorator_factory(sap="=")
def my_sorted(*args, **kwargs):
    return sorted(*args, **kwargs)


m = my_sum(1, 2)
print(m)
print(my_sorted([1, 2, 3, "4"], key=lambda x: int(x)))