def reverse(st):
    words = st.split()
    words.reverse()
    reversed_string = ' '.join(words)
    print (reversed_string)
reverse('Hello World.')
