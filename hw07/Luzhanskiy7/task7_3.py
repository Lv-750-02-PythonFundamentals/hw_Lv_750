def calculates_num(word = ''):
    word = input('Enter the word: ')
    d = {word[i]: word.count(word[i]) for i in range(len(word))}
    print(d)

calculates_num()