# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# Simple: Find The Distance Between Two Points
from math import sqrt
def distance(x1, y1, x2, y2):
    return round(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)

# No yelling!
def filter_words(st):
    a = st.lower()
    b = a.capitalize()
    return " ".join(b.split())

# Convert a Number to a String!
def number_to_string(num):
    return str(num)

# Reversing Words in a String
def reverse(st):
    a = st.split()
    a.reverse()
    st = " ".join(a)
    return st

# Reverse List Order
def reverse_list(l):
    return l[::-1]

# Multiples of 3 or 5
def solution(number):
    sum = 0
    if number < 0:
        return 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0 and i < number:
            sum += i
    return sum

# Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if mpg * fuel_left >= distance_to_pump:
        return True
    else:
        return False
    
# Are You Playing Banjo?
def are_you_playing_banjo(name):
    if name.lower().startswith("r"):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# Convert boolean values to strings 'Yes' or 'No'.
def bool_to_word(boolean):
    return "Yes" if boolean is True else "No"

# Counting sheep...
def count_sheeps(sheep):
    return sheep.count(True)

# Is this my tail?
def correct_tail(body, tail):
    return True if body.endswith(tail) else False
