PYTHON_ZEN = """
The Zen of Python, by Tim Peters

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
Namespaces are one honking great idea -- let's do more of those!

"""


def edit_text(text: str, word1: str, word2: str, word3: str):
    word1_count = text.count(word1)
    word2_count = text.count(word1)
    word3_count = text.count(word3)
    return f"Number of occurrences of the word '{word1}': {word1_count}\n" \
           f"Number of occurrences of the word '{word2}': {word2_count}\n" \
           f"Number of occurrences of the word '{word3}': {word3_count}\n\n" \
           f"Edited text:\n {text.replace('i', '&').upper()}"


def edit_number(number: int):
    str_number = str(number)
    digit_production = 1
    for char in str(number):
        digit_production *= int(char)
    return f"digit_production = {digit_production}\n" \
           f"reversed_number = {int(str_number[::-1])}\n" \
           f"sorted_number = {int(''.join(sorted(str_number)))}"


def change_variables(var1, var2):
    var1, var2 = var2, var1
    return f"variable 1 = {var1}\nvariable_2 = {var2}"


if __name__ == "__main__":
    print(change_variables(3, 15))
    print(edit_number(5612))
    print(edit_text(PYTHON_ZEN, "better", "never", "is"))
