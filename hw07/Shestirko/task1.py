def largest_num(num1, num2):
    """ The function returns the largest number among two given numbers
    
    num1: 1st given number (int or float)
    num2: 2nd given number (int or float)
    """

    if num1 > num2:
        return num1
    else:
        return num2
    
    print(largest_num.__doc__)