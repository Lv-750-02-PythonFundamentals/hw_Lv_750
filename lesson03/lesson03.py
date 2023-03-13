# a = 1
# print(id(a))
# a = 22
# print(id(a))
# a = 1
# print(id(a))
# a = (1,2,3)
#
# a = [21,2,3]
# print(id(a), a)
# a.append(55)
# a.sort()
# print(id(a), a)
# a = [1,2,3]
# print(id(a))
#
#
# a = 1
# print(type(a) is int)
# print(isinstance(a, int))
# a = {}
# print(type(a) is int)
# print(isinstance(a, int))
#
#
# class A: pass
#
#
# class B(A): pass
#
#
# a_1 = A()
# a_2 = B()
# print(isinstance(a_1, A))
# print(isinstance(a_2, B))
# print(isinstance(a_2, A))
# print(type(a_2) is A)
# print(type(a_2) is B)
#
# a = [1 + 2 +
#      3 + 4 + 6
#      + 6]
# print(type(a), a)
# a = {1 + 2 +
#      3 + 4 + 6
#      + 6}
# print(type(a), a)
# a = ()
# print(type(a), a)
# a = (1 + 2 +
#      3 + 4 + 6
#      + 6)
# print(type(a), a)
# a = (1 + 2 +
#      3 + 4 + 6
#      + 6, )
# print(type(a), a)

# for (;;) { begin
#     a= 1;
#     b = 2
# } end
# a = 0
# N = 5
# for i in range(N):
#     a += i
#     print(f"{i=} {a=}")
#     for j in range(i, N):
#         a *=j
#         print(f"\t {j=} {a=}")
#
# print("end")

#
# a = "test"
# b = 25
# c = [1, 2, 3]
# a, b, c = "test", 25, [1, 2, 3]
# a, b, c, d = "test", 25, [1, 2, 3], 22

# a = [1, 2, 3]
# b = a
# c = b
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)
# b[0] = 99
# print(id(a), a)
# print(id(b), b)
# print(id(c), c)
# a = b = c = [1, 2, 3]

# b = 0b1111
# print(b)
# b = 15
# print(b)
# b = 0o17
# print(b)
# b = 0xF
# print(b)
# print(0.3+0.3+0.3)
#
# from decimal import Decimal
# a = Decimal('0.3')+Decimal('0.3')+Decimal('0.3')
# print(a)

# a = True
# b = False
# print(a, b)

# l = []
# print(type(l), l)
# l = [1, 5.6, 6]
# print(type(l), l)
# l = list()
# print(type(l), l)
# l = list("12345abc")
# print(type(l), l)

# # s = {}
# # print(type(s), s)
# s = {1, 1, 1, 1, 1, 2, 3}
# print(type(s), s)
# s = set()
# print(type(s), s)
# s = set("12345abc")
# print(type(s), s)

# d = {}
# print(type(d), d)
# d = {"a": "a", 1: "a"}
# print(type(d), d)
# d = dict()
# print(type(d), d)
# d = dict([(1, 1), (2, 2), (3, 3)])
# print(type(d), d)
#
# a = "abc"
# print(a.__hash__())
#
# d = {(1, 2, 3): 11}
# print(d)
# a = 9**4300
# print(len(str(a)))
# print(int("012345", 6))
# print(int("z", 36))
# for i in range(1000):
#     print(i, chr(i))
#
# for i in "range(1000)":
#     print(i, ord(i))
#
# a = """test
# test
# test
# """
# print(a)
# a = '''test
# test
# test
# '''
# print(a)
# a = 'test\ntest\ntest\u2764'
# print(a)
# name = "John "
# age = 23
# print("%s is %d years old." % (name, age))
# print(f"{name} is {age} years old.")

str = 'programiz'
print('str = ', str)
#first character
print('str[0] = ', str[0])
#last character
print('str[-1] = ', str[-1])
#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
print('str[:] = ', str[:])
print('str[3:] = ', str[3:])
print('str[3:] = ', str[::2])
print('str[3:] = ', str[::-1])
#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])