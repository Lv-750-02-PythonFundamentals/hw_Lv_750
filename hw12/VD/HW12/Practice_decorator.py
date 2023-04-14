"""Using several decorators, create a sandwich consisting of
lettuce, tomatoes and meat.
<\ ^^^^^^^ />
# tomato #
- meat-
~ salad ~
<\ ______ />
"""

def sandwich(func):
    def wrapper():
        print("<\ ^^^^^^^ />")
        func()
        print("<\ ______ />")
    return wrapper

def tomato_salad(func):
    def wrapper():
        print("# tomato #")
        func()
        print("~ salad ~")
    return wrapper


@sandwich
@tomato_salad
def meat():
    print("- meat-")

meat()