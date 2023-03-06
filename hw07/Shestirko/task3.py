def count_characters(string):
    char_dict = {}
    for char in string:
        char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict


string = input("Enter your string to count characters: ")
print(count_characters(string))