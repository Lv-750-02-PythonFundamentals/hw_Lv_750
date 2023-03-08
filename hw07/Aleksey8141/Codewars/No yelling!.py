def filter_words(st):
    st = ' '.join(st.split())  # заміна кількох пробілів на один
    st = st.lower().capitalize()  # перетворення в нижній регістр, а потім перша літера велика
    return st
