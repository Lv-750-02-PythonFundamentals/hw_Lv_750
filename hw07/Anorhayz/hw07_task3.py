user_string = input("Please enter your phrase: ")


def char_freq(user_phrase):
    char_frequency = {}
    for element in user_phrase:
        if element in char_frequency:
            char_frequency[element] += 1
        else:
            char_frequency[element] = 1
    return str(char_frequency)


print(char_freq(user_string))
