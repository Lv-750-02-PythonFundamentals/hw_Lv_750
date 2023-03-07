def get_largest_number(a, b):
    """
    Returns the largest number of two numbers.

    Parameters:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: The largest of the two numbers.

    """
    if a > b:
        return a
    else:
        return b

print(get_largest_number(132, 211))