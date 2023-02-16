text = """The Zen of Python, by Tim Peters
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
Namespaces are one honking great idea -- let's do more of those!"""


# split the text into a list of words
words = text.split()

# initialize counters
better_count = 0
never_count = 0
is_count = 0

# iterate over each word in the list and increment the appropriate counter
for word in words:
    if word == "better":
        better_count += 1
    elif word == "never":
        never_count += 1
    elif word == "is":
        is_count += 1

print("Number of occurrences of 'better':", better_count)
print("Number of occurrences of 'never':", never_count)
print("Number of occurrences of 'is':", is_count)
