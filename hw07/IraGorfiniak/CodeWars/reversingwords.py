def reverse(st):
    words = st.split(' ')

    reverse_string = ' '.join(reversed(words))

    return reverse_string


print(reverse('Ira Gorfiniak'))
