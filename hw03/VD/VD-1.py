# You need to write Python's philosophy in the string format:
python_philosofy = """Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!"""

# - find separately the number of occurrences of the words - "better", "never" and "is" in the given line
print(f'better counted {python_philosofy.count("better")} times', f'never counted {python_philosofy.count("never")} times', f'is counted {python_philosofy.count("is")} times', sep="\n", end="\n\n")

# - you need to display all text in uppercase (all letters in uppercase)
print(python_philosofy.upper(), end="\n\n")

# - replace all occurrences of the symbol “i” with “&”
print(python_philosofy.replace("i", "&"))

