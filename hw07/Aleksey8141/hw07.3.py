'''Write a function that calculates the number of characters
included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}
'''

def calc_char():
    string = input('Введіть слово: ')
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)
calc_char()
