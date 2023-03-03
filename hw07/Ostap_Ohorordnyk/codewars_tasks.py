#task1 Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

#task2 Simple: Find The Distance Between Two Points

import math
def distance(x1, y1, x2, y2):

    return round(math.sqrt((x1-x2)**2 + (y1-y2)**2), 2)

# task3 No yelling!

def filter_words(st):
    st = st.lower()

    return st[0].title() + st[1:]

#task4 Convert a Number to a String!

def number_to_string(num):
    return str(num)

#task5 Reversing Words in a String

def reverse(st):
    text = []
    for word in st.split():
        text.append(word)

    reversed_words = []

    while text:
        reversed_words.append(text.pop())

    reversed_string = " ".join(reversed_words)

    return reversed_string
#task 6 Reverse List Order

def reverse_list(l):
  return l[::-1]

# task 7 Multiples of 3 or 5

def solution(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)

#task 8 Will you make it

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return True if distance_to_pump <= (mpg *fuel_left) else False

#task 9 Are You Playing Banjo

def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"
#task 10 Convert boolean values to strings 'Yes' or 'No'

def bool_to_word(boolean):
    return "Yes" if boolean else "No"

#task 11 Counting sheep...

def count_sheeps(sheep):
    amount = 0
    for i in sheep:
        if (i == True):
            amount += 1
    return amount

#task 12 Is this my tail?

def correct_tail(body, tail):
    return body[-1] == tail

