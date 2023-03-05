# Task3. Write a function that calculates the number of characters
# included in a given string
# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def calculates_number_characters(word):
    occurrenc_letters={}

    for letter in word:
        if letter not in occurrenc_letters:
            occurrenc_letters[letter] = 1
        else:
            occurrenc_letters[letter] += 1 
    return occurrenc_letters

word=input('Enter you word to calculate the number of characters:')
print(calculates_number_characters(word))

