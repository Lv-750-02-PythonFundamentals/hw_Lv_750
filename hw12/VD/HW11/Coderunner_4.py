"""Write the function check_odd_even (number) whose input parameter is an integer number. The function checks whether the set number is even or odd:

in the case of an even number the function should be displayed the corresponding message - "Entered number is even";
in the case of an odd number the function should be displayed the corresponding message - "Entered number is odd";
in the case of incorrect data the function should be displayed the message - "You entered not a number."
Note: in the function you must use the try except construct.
"""

def check_odd_even(number):
    try: 
        number = int(number)
        if number % 2:
            result = "Entered number is odd"
        else:
            result = "Entered number is even"
    except ValueError as e:
        result = "You entered not a number."

    return result

print(check_odd_even("abc"))
    