# t1 = (1, 2, 3)
# t2 = (1, 2, 3)
# print(id(t1), t1.__hash__())
# print(id(t2), t2.__hash__())
# print()
# class A:
#     """"""
#     def __hash__(self):
#         return 10
#
#     def __eq__(self, other):
#         return self.__hash__() == other.__hash__()
#
# t1 = A()
# t2 = A()
# print(id(t1), t1.__hash__())
# print(id(t2), t2.__hash__())
# d = {t1: 1,
#      t2: 2}
# print(d)

# List
# l = list()
# print(type(l), l)
# l = list("test")
# print(type(l), l)
# l = []
# print(type(l), l)
# l = [1, "bfjds", False, 2.2]
# # print(type(l), l)
#
# print([method for method in dir(list) if not method.startswith("_")])
# l = []
# for method in dir(list):
#     if not method.startswith("_"):
#         l.append(method)
# l = []
# l.append(12)
# l.append([1, 2])
# print(l)
# l.clear()
# print(l)
# l = []
# print(l)
#
# l1 = [1, 2]
# l2 = [3, 4]
# l = [l1, l2]
# print(l)
# l1.clear()
# l2 = []
# print(l)
# print(l2)
# l = [1,2,3,4]
# l2 = l
# l3 = l.copy()
# print(l, l2, l3)
# print(id(l), id(l2), id(l3))
# l = ["a", "b"]
# l1 = [1, 2, 3, 4, l]
# l2 = l1.copy()
# print(l1)
# print(l2)
# l1[1] = 99
# l2[2] = -1
# l1[4][0] = "A"
# print(l1)
# print(l2)
#
# from copy import deepcopy
#
# l = ["a", "b"]
# l1 = [1, 2, 3, 4, l]
# l2 = deepcopy(l1)
# print(l1)
# print(l2)
# l1[1] = 99
# l2[2] = -1
# l1[4][0] = "A"
# print(l1)
# print(l2)

# l = [1, 2, 3, 4, 5, 67, 1, 2, 45, 2, 4, 6]
# print(l.count(1))
# print(l.count("1"))
# l = [1, 2, 3]
# l1 = [3, 4, 5]
# l.append(l1)
# print(l)
# l.extend(l1)
# print(l)
# print(l.index(3))
# print(l.index(3, 3))
# print(l.index("3, 3"))

# l = list(range(10))
# print(l)
# l.insert(3, "a")
# print(l)
# print(l.pop())
# print(l)
# print(l.pop(2))
# print(l)
# # print(l.pop(22))
# # print(l)
# l = l+l
# print(l)
# l.remove('a')
# print(l)
# # l.remove('a')
# # l.remove('a')
# print(l)
# l.reverse()
# print(l)
# print(list(reversed(l)))
# print(l)
# l.sort(key= lambda x: x if type(x) is int else ord(x))
# print(l)
# l = [(i, j, k) for i in range(3) for j in range(i, 5) for k in range(i, j)]
# print(l)
# for i in l:
#     print(i)
#
# l = []
# for i in range(3):
#     for j in range(i, 5):
#         for k in range(i, j):
#             l.append((i, j, k))
# print(l)
# for i in l:
#     print(i)

# Tuple
# print([method for method in dir(tuple) if not method.startswith("_")])
# t = tuple()
# t = tuple("bdsk")
# t = ()
# print(t)
# t = (1)
# print(t)
# t = (1,)
# print(t)
# t = (1, 2, 3, "sdaf")
# print(t)
#
# t = (1, 2, [3, 4])
# t[2][0] = "X"
# print(t)
# t[2] = "X"


# # Set
# print([method for method in dir(set) if not method.startswith("_")])
# # s = set()
# # print(type(s), s)
# # s = set("dsvfhsbdjzdbsfvzsjhvfhgsavfjhasvfjas")
# # print(type(s), s)
# # s = {1, 2, 3, 1}
# # print(type(s), s)
# # s = {}
# # print(type(s), s)
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print(s1.difference(s2))

# Dict
# print([method for method in dir(dict) if not method.startswith("_")])
# d = dict()
# print(type(d), d)
# d = dict({"a": 1, "b": 2})
# print(type(d), d)
# d = dict([(1, 2), ["a", "b"], ("dsjhvfdsjh", 5), "cd", {"x", "y"}])
# print(type(d), d)
# d = {}
# print(type(d), d)
# d = {"key1": "value1",
#      2: [12, 55],
#      (1, 2, 3): {1: 2}}
# print(type(d), d)
# l = [1,23]
# d = {"key1": "value1",
#      2: [12, 55],
#      (1, 2, l): {1: 2}}
# d = {"key1": "value1",
#      2: [12, 55],
#      (1, 2, 3): {1: 2}}
# # print(d["key1"])
# print(d[2])
# print(d[(1, 2, 3)])
# d[(1, 2, 3)] = [1,2,3]
# print(d)
# # d["(1, 2, 3)"]
# print(d.get((1, 2, 3)))
# print(d.get("(1, 2, 3)"))
# print(d.get("(1, 2, 3)", "XY"))
# d2 = d.fromkeys("abcdefg", [1,2,3,4,5,6])
# print(d2)
# print(list(d2.items()))
# for key, value in d2.items():
#      print(key, value)
# print(d)
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d.pop("key1"))
# print(d)
# print(d.popitem())
# print(d)
# d.setdefault("key122", "tets")
# print(d)
# d.update({"a":"a", "b":"a", "c":"a"})
# print(d)
#
# l = [i for i in range(10)]
# print(type(l), l)
# l = {i for i in range(10)}
# print(type(l), l)
# l = {i:i*5 for i in range(10)}
# print(type(l), l)


# l = (i for i in range(10))
# print(type(l), l)
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
# print(next(l))
l = [i for i in range(99999)]
g = (i for i in range(99999))
print(l.__sizeof__())
print(g.__sizeof__())

for i in l:
    if i > 99995:
        print(i)

for i in g:
    if i > 99995:
        print(i)
