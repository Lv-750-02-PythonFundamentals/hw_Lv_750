"""Create a module with functions of addition, subtraction,
multiplication, division. And in another module - calculator.py, it is
necessary to ask the user what action he wants to perform and
with what numbers and perform the necessary actions.
"""

def addition(numbs: list) -> int:
    """returns addition of entered integers, can accept ublimited numbe of integers"""
    summa = 0
    for i in numbs[0:-1]:
        summa += int(i)
    return summa


def multipl(numbs: list) -> int:
    """returns multiplication of entered integers, can accept unlimited number of arguments"""
    mult = 1
    for i in numbs[0:-1]:
        mult *= int(i)
    return mult


def substr(numbs: list) -> int:
    """return substraction of entered integers, can accept unlimited number of arguments by entered sequence"""
    subs = int(numbs[0])
    for i in numbs[1:-1]:
        subs -= int(i)
    return subs


def division(numbs: list) -> int:
    """return division of entered integers, can accept unlimited number of arguments by entered sequence"""
    div = int(numbs[0])
    for i in numbs[1:-1]:
        if int(i) == 0:
            return "Ooops, zeros not allowed"
        div /= int(i)
    return div

