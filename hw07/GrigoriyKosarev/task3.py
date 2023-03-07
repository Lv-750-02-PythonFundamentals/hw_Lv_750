"""
Task3. Write a function that calculates the number of characters
included in a given string
• input: "hello"
• output: {"h":1, "e":1,"l":2,"o":1}
"""

def calculate_str_symbols(input="hello"):
    result = {}
    for i in input:
        value = result.get(i)
        if value == None:
            result.update({i: 1})
        else:
            result.update({i: value + 1})
    return result

print(calculate_str_symbols())
