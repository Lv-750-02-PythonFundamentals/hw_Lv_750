# index_i = 1
# index_j = 1
# while index_i < 10:
#     print(index_i, end="\n\t")
#     index_i += 2
#     while index_j < index_i:
#         print(index_j, end=" ")
#         index_j += 1
#     print()
#     # if index_j > 20:
#     #     k = 1
#
# # print(k)
import random

# index_i = 1
#
# while index_i < 10:
#     print(index_i, end="\n\t")
#     index_i += 2
#     index_j = 1
#     while index_j < index_i:
#         print(index_j, end=" ")
#         index_j += 1
#     print()


# l = 123
# for i in l:
#     print(i)
# l = [1, 2, 3, 4, 5]
# for element in l:
#     print(element)
# l = "TestMyName"
# for element in l:
#     print(element)

# s = set()
# s.update("a")
# s.update("c")
# s.update("b")
# s.update("d")
# print(s)
# for i in s:
#     print(i)
# print(element)
# d = {}
# d["c"] = 1
# d["d"] = 1
# d["b"] = 1
# d["a"] = 1
# # print(d)
# # for i in d:
# #     print(i)
# d["aa"] = 4
# d["a"] = 4
# print(d)
# for key in d:
#     print(key, d[key])
# print(d.items())
# key, value = list(d.items())[0]
# print(key, value)
#
# for key, value in d.items():
#     print(key, value)

# for _ in range(999):
#     number = input("enter number:")
#     try:
#         number = int(number)
#         break
#     except:
#         pass
# print(number)
# while True:
#     number = input("enter number:")
#     try:
#         number = int(number)
#         break
#     except:
#         pass
# number = ""
# while type(number) is not int:
#     number = input("enter number:")
#     try:
#         number = int(number)
#     except:
#         pass
# print(number)


# number = 0
# while number < 10:
#     number = int(input("enter number:"))
#
# print(number)

# random_list = []
#
# for i in range(random.randint(1, 30)):
#     random_list.append(random.randint(0, 20))
#
# print(random_list)
# while sum(random_list) > 100:
#     delited_element = random_list.pop()
#     print(f"delited {delited_element}")
#
# print(random_list)

# for i in range(len(random_list)):
#     if sum(random_list) < 100:
#         break
#     delited_element = random_list.pop()
#     print(f"delited {delited_element}")
# print(random_list)

# r = range(3)
# print(r)
# print(list(r))
# r = list(range(3, 17))
# print(r)
# r = list(range(-33, 17, 4))
# print(r)
l = [1, 2, 3, 4, 667, 6]
for i in range(len(l)):
    if l[i] % 2:
        print(f"l[{i}]={l[i]} is odd")

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(matrix)
# for i in range(len(matrix)):
#     print(matrix[i])
# for line in matrix:
#     print(line)
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end="\t")
#     print()
# for row in matrix:
#     for element in row:
#         print(element, end="\t")
#     print()
#
# l = list(range(10))
# print(l)
# s = 0
# for i in range(len(l)):
#     s += l[i]
#     print(s)
#     if s > 10:
#         break
#     l[i] **=3
# print(l)
#
# l = list(range(10))
# print(l)
# for i in range(len(l)):
#     print(i)
#     if l[i] % 2:
#         continue
#     print(f"{l[i]=}", end=" => ")
#     l[i] **=2
#     print(f"{l[i]=}")
# print(l)

for i in range(2):
    break
else:
    print("b good")


for i in range(2):
    continue
else:
    print("c good")