# # a = 10
# # b = 20
# # c = 30
# #
# # print(a<b and b < c)
# # print(a < b < c)
# # a = 10
# # b = 20
# # c = 5
# # print(a < b > c < a)
# # print(True and True or False) #=> (True or False)
# # print(True or True and False) #=> (True or False)
# #
# # print(10 and [1,2] and "gdh")
# # print(10 and [1,2] and ["gdh"])
# # print(10 and [1,2] and None and ["gdh"])
# # print(10 and [1,2] and None and "")
# # print(10 and [1,2] and "" and None)
# # print(10 or [] or "" or None)
# # print(0 or [] or "" or None)
# # print(0 or [] or "a" or None)
# # 0, "", [], {}, {}, None, False
# a = 10
# print(a is True)
# print(a is int)
# print(type(int))
# b = 11
# print(a is b)
# b = 10
# print(a is b)
# print(id(a))
# print(id(b))
#
# a = [1,2,3]
# b = [1,2,3]
# print(id(a))
#
# print(id(b))
# print(a is b)
# #
# # class A():
# #     pass
# #
# # a = A()
# # print(a)
# # print(a.__hash__())
# # print(id(a))
#
# print("-"*10)
# a = 9999**999
# print(a.__hash__())
# print(id(a))
# a = 9999**999
# print(a)
# print(a.__hash__())
# print(id(a))

# st = "testtesttest"
# print("tt" in st)
# print("t8" in st)
# print([1,2,3] in [1, [1,2,3], 2])

# a = 10
# print(a in int)

# a = 109
# print('9' in str(a))
# print('8' in str(a))
#
# score = 12
# if score > 8:
#     print("1-You have passed the exam")
#     print("1")
# print("Exam was finished.")
# if score < 8:
#     print("2-You have passed the exam")
#     print("2")
# print("Exam was finished.")


# temperature = int(input('What is the temperature? '))
# if temperature > 30:
#     print('Wear shorts.')
# else:
#     print('Wear long pants.')
# print('Get some exercise outside.')
#
# age = int(input("age: "))
# if age < 12:
#     print('kid')
# elif age < 18:
#     print('teenager')
# elif age < 50:
#     print('adult')
# else:
#     print('you are not old')
#
# if age < 12:
#     print('kid')
# else:
#     if age < 18:
#         print('teenager')
#     else:
#         if age < 50:
#             print('adult')
#         else:
#             print('you are not old')

# weather = "raining"
# msg = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# print(msg)
# weather = "son"
# msg = "Open Your umbrella" if weather == "raining" else "Wear your cap"
# print(msg)
# # msg = weather == "raining" ? "Open Your umbrella" : "Wear your cap"
#
# age = int(input("age: "))
# msg = 'kid' if age < 12 else 'teenager' if age < 18 else 'adult' if age < 50 else 'you are not old'
#
# if weather == "raining":
#     msg = "Open Your umbrella"
# else:
#     msg = "Wear your cap"
# status = int(input("status code: "))
# match status:
#     case 400:
#         print("Bad request")
#     case 401:
#         print("nauthorized")
#     case 403:
#         print("Forbidden")
#     case 404:
#         print("Not found")
#     case _:
#         print("Other error")
#
#
# if status == 400:
#     print("Bad request")
# elif status == 401:
#     print("nauthorized")
# elif status == 403:
#     print("Forbidden")
# elif status == 404:
#     print("Not found")
# else:
#     print("Other error")
#
#
# if status == 400:
#     print("Bad request")
# else:
#     if status == 401:
#         print("nauthorized")
#     else:
#         if status == 403:
#             print("Forbidden")
#         else:
#             if status == 404:
#                 print("Not found")
#             else:
#                 print("Other error")

