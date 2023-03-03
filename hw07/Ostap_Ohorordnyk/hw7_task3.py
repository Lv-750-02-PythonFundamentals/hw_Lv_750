def counting_letters():
    """Function that calculates the number of characters
       included in a given string"""
    text = list(input("Enter a text : "))
    result = {}
    for i in text:
        result[i] = text.count(i)

    print("Number of unique characters included in the given text", result)

counting_letters()

