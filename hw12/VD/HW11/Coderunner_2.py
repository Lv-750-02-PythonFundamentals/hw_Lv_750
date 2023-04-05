"""Write your code bellow to create custom Error named InputError and function check.

The error must save description of error in data attribute.

In data of error must be written:

"Short text error" if length of string less than 3,
"Long text error" if length of string more than 15,
"Type text error" if we try to check not string.
Your function check will be called from function test_input as shown on screenshot.
"""

class InputError(Exception):
    def __init__(self, data):
        self.data = data
     
    def __str__(self):
        return self.data
        

def check(text):
    if len(text) < 3 and type(text) is str:
        data = "Short text error"
    elif len(text) > 15 and type(text) is str:
        data = "Long text error"
    elif type(text) != str:
        data = "Type text error"
    else:
        data = True
    return data

def test_input(text):
    try:
        print(check(text))
    except InputError as e:
        print(e.data)

test_input("Long text that can not be placed in some document")