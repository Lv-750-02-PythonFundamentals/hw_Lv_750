philosophy_of_python = """
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those! """

count_word_better = philosophy_of_python.count("better")
print(f"the word 'better' appears in the text {count_word_better} times ")

count_word_never = philosophy_of_python.count("never")
print(f"The word 'never' appears in the text {count_word_never} times")

count_word_is = philosophy_of_python.count("is")
print(f"The word 'is' appears in the text {count_word_is} times")

upper_all_text = philosophy_of_python.upper()
print(upper_all_text)

replace_letters_in_text = str(philosophy_of_python).replace("i", "&")
print(replace_letters_in_text)
