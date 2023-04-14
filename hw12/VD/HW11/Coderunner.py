"""Write the function check_positive(number)whose input parameter is a number. The function checks whether the set number is positive or negative:

in the case of a positive number the function should be displayed the corresponding message - "You input positive number: input parameter of function"
in the case of a negative parameter the function should return the exception of your own class MyError and displayed the corresponding message. "You input negative number: input parameter of function. Try again."
in the case of incorrect data the function should be displayed the message - "Error type: ValueError!"
"""

class MyError(Exception):
    def __init__(self, data):
        self.data = data
        
    def __str__(self):
        return self.data
        # return repr(self.data)
    
    
def check_positive(number):
    try:
        number = float(number)
        if float(number) > 0:
            result = f"You input positive number: {(number)}"
        else:
            raise MyError(f"You input negative number: {(number)}. Try again.")
    except MyError as my_e:
        result = my_e
    # except TypeError as e:
        # result = "Error type: ValueError!"
    except ValueError:
        result = "Error type: ValueError!"
    return result

print(check_positive("abc"))
    # enter your code