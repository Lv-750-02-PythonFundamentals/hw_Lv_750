# a = [5, 6, 7, 8]
# try:
#     print("Second element = {}".format(a[1]))
#     # Throws error since there are only 4 elements in array
#     print("Fifth element = {}".format(a[4]))
# except IndexError as e:
#     print(e)

#
# def red_int(msg):
#     while True:
#         x = input(msg)
#         # x = int(x)
#         # return x
#         try:
#             x = int(x)
#             return x
#         except:
#             print("is not number")
# i = red_int("x: ")

# def div(a, b):
#     result = 1
#     try:
#         result = a / b
#     except ZeroDivisionError as e:
#         print("ZeroDivisionError", e)
#     except ArithmeticError as e:
#         print("ArithmeticError", e)
#     except TypeError as e:
#         print("TypeError", e)
#     else:
#         print("Ura")
#         return result
#     finally:
#         print("finally")

#
# div(5, 0)
# div("5", 5)
# div(4, 5)
import logging

logging.basicConfig(filename='app.log',
                    filemode='w',
                    format='%(process)d-%(levelname)s-%(asctime)s-<<<%(message)s>>>',
                    level=logging.INFO)

logging.debug('This will get logged debug')
logging.error('This will get logged error')
logging.info('This will get logged- info')
logging.critical('This will get logged critical')
logging.warning('This will get logged warning')


class MyError(Exception):
    pass


def div(a, b):
    result = 1
    if b == 0:
        raise MyError("AAAAAAAAAAAAAAAAA!!!!!!!!!!!!!!")
    return a / b


try:
    div(1, 0)
except MyError as e:
    print(e)

div(1, 0)
