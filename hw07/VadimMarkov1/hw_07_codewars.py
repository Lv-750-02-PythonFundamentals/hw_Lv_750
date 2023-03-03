def greet(name):
    """Jenny's secret message"""
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


def distance(x1, y1, x2, y2):
    """Find The Distance Between Two Points"""
    return round(((x2-x1)**2 + (y2-y1)**2)**0.5, 2)


def filter_words(st):
    """No yelling!"""
    s = st.strip()
    words = s.split()
    words = [words[0].capitalize()] + [w.lower() for w in words[1:]]
    return ' '.join(words)


def number_to_string(num):
    """Convert a Number to a String!"""
    return str(num)


def reverse(st):
    """Reversing Words in a String"""
    s = st.strip().split()
    return " ".join(reversed(s))


def reverse_list(l):
    """Reverse List Order"""
    return list(reversed(l))


def solution(number):
    """Multiples of 3 or 5"""
    return sum([x for x in range(number) if x > 0 and x%3 == 0 or x%5 == 0])


def zero_fuel(distance_to_pump, mpg, fuel_left):
    """Will you make it?"""
    return mpg*fuel_left >= distance_to_pump


def are_you_playing_banjo(name):
    """Are You Playing Banjo?"""
    return f"{name} plays banjo" if name[0].lower() == "r" else f"{name} does not play banjo"


def bool_to_word(boolean):
    """Convert boolean values to strings 'Yes' or 'No'."""
    return "Yes" if boolean else "No"


def count_sheeps(sheep):
    """Counting sheep..."""
    return len([x for x in sheep if x])


def correct_tail(body, tail):
    """Is this my tail?"""
    return body[-1] == tail
