"""
Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. 
String should be capitalized and properly spaced. Using re and string is not allowed.
"""

def filter_words(st):
    words = [w for w in st.split(' ') if w != '']
    return " ".join(words).capitalize()