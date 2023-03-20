def calculate_characters(string):
    calculate = {}
    for i in string:
        if i in calculate.keys():
            calculate[i] += 1
        else:
            calculate[i] = 1
    return calculate


print(calculate_characters("hello"))