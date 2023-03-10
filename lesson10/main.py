print("Hello!", end=" ")
print(dir())
import module

print(dir())
print("Good by!", end="")
my_func = lambda x: x if x > 5 else x ** 2 * my_func(10)

my_func(2)


def my_func(x):
    return x if x > 5 else x ** 2 * my_func(10)


def my_func(x):
    if x > 5:
        return x
    else:
        return x ** 2 * my_func(10)
