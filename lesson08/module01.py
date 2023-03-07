"""
my module01
"""
# __all__ = ["a", "my_funk"]
a = 1


def my_funk():
    print("my_func")


def my_mane():
    print(__name__)


def _my_mane():
    print(__name__)


def __my_mane():
    print(__name__)


if __name__ == "__main__":
    print("module name: ", __name__)
