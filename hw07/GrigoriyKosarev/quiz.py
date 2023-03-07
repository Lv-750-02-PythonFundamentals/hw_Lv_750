
def functionName():
    """
    test
    :return:
    """

# print(functionName.__doc__)

def output_param(x, y, z):
    print(x, y, z)

my_tuple = (1, 2, 3)
output_param(*my_tuple)

my_func = lambda x: x if x>5 else x**2*my_func(10)

# print(my_func(2))

my_list = [lambda x: x**2,
           lambda x: x**3,
           lambda x: x**4]

for item in my_list:
    1
    # print(item(5))

def my_func1(first_param = 3, second_param = 1):
    first_param = first_param + second_param
    second_param += 1
    print(first_param, second_param)

my_func1(second_param = 1, first_param = 3)