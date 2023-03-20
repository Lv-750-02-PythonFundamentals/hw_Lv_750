def maximum(a, b):
    """
    Description : Object initialisation

    :param a: First number to compare
    :type a: str

    :param b: Second number to compare
    :type b: str
    """
    if a >= b:
        return a
    else:
        return b


a = input('Enter first number: ')
b = input('Enter second number: ')

print('Larger number is:', maximum(a, b))
