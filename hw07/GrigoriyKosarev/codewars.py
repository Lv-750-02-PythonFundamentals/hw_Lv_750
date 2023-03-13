# 1. Jenny's secret message
# https://www.codewars.com/kata/55225023e1be1ec8bc000390
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    return "Hello, {name}!".format(name=name)

# 2. Simple: Find The Distance Between Two Points
# https://www.codewars.com/kata/simple-find-the-distance-between-two-points
def distance(x1, y1, x2, y2):
    return round(((x2 - x1)**2 + (y2 - y1)**2)**0.5, 2)

# 3. No yelling!
# https://www.codewars.com/kata/no-yelling
def filter_words(st):
    return st.capitalize()

# 4. Convert a Number to a String!
# https://www.codewars.com/kata/convert-a-number-to-a-string
def number_to_string(num):
    return str(num)

# 5. Reversing Words in a String
# https://www.codewars.com/kata/reversing-words-in-a-string
def reverse(st):
    reverse_str = st.split(" ")
    reverse_str.reverse()
    return reverse_str

# 6. Reverse List Order
# https://www.codewars.com/kata/reverse-list-order
def reverse_list(l):
    l.reverse()
    return l

# 7. Multiples of 3 or 5
# https://www.codewars.com/kata/multiples-of-3-or-5
def solution(number):
    i = 0
    summ = 0
    while (i < number):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
        i += 1
    return summ

# 8. Will you make it?
# https://www.codewars.com/kata/will-you-make-it
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return distance_to_pump / mpg <= fuel_left

# 9. Are You Playing Banjo?
# https://www.codewars.com/kata/are-you-playing-banjo
def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    return f"{name} does not play banjo"

# 10. Convert boolean values to strings 'Yes' or 'No'.
# https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no
def bool_to_word(boolean):
    return "Yes" if boolean else "No"

# 11. Counting sheep...
# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i:
            count += 1
    return count

# 12. Is this my tail?
# https://www.codewars.com/kata/is-this-my-tail/train/python
def correct_tail(body, tail):
    sub = body[len(body)-1]
    if sub == tail:
        return True
    return False

# print(correct_tail("Fox", "x"))