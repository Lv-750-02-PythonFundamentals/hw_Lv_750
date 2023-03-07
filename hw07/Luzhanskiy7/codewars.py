def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


def distance(x1, y1, x2, y2):
    total = ((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5
    return round(total, 2)


def filter_words(st):
    capit = st.capitalize()
    return capit


def number_to_string(num):
    strin = str(num)
    return strin


def reverse(st):
    st_p = st.partition(' ')
    st_l = list(st_p)
    st_l.pop(1)
    st_l.reverse()
    st_str = ' '.join(st_l)
    return st_str


def reverse_list(l):
    return l[::-1]


def solution(number):
    count = 0
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            count += i
    return count


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    else:
        return False


def are_you_playing_banjo(name):
    if name[0] == 'R' or name[0] == 'r':
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'


def bool_to_word(boolean):
    if boolean == True:
        return 'Yes'
    elif boolean == False:
        return 'No'


def count_sheeps(sheep):
    count = 0
    for i in range(len(sheep)):
        if sheep[i] == True:
            count += 1
    return count


def correct_tail(body, tail):
    if body[-1] == tail:
        return True
    else:
        return False



