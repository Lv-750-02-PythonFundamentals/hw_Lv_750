"""Write a function that calculates the number of characters
included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}
"""

def character(some_str: str):
    some_dic = {}
    for i in some_str:
        some_dic.update(some_dic.fromkeys(i, some_str.count(i)))
    print(some_dic)
    return some_dic

character("Hello, how are you?")