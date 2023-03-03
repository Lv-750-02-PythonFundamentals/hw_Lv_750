"""
Create a function that returns the mean of all digits.

The mean of all digits is the sum of digits / how many digits there are (e.g. mean of digits in 512 is (5+1+2)/3(number of digits) = 8/3=3).
The mean will always be an integer.
"""
def mean(number):
    sum = 0
    count = 0
    for i in str(number):
        sum += int(i)
        count += 1
    return round(sum / count)

# print(mean(512))
"""
Create a function that takes a string and returns the number (count) of vowels contained within it.
Notes:
- a, e, i, o, u are considered vowels (not y).
- All test cases are one word and only contain letters.
"""
def count_vowels(word):
    if str(word).isalpha():
        count = 0
        for i in word:
            if i == "a":
                count += 1
            elif i == "e":
                count += 1
            elif i == "i":
                count += 1
            elif i == "o":
                count += 1
            elif i == "u":
                count += 1
        return count
    return 0

# print(count_vowels("asdfoudfsife"))
"""
Create a function which returns a list of booleans, from a given number. Iterating through the number one digit at a time, append True if the digit is 1 and False if it is 0.
Notes. Expect numbers with 0 and 1 only.
"""
def integer_boolean(binary_number):
    result =[]
    for i in binary_number:
        if i == "0":
            result.append(False)
        elif i == "1":
            result.append(True)
    return result

# print(integer_boolean("01010101"))

"""
An isogram is a word that has no duplicate letters. Create a function that takes a string and returns either True or False depending on whether or not it's an "isogram".
Notes:
- Ignore letter case (should not be case sensitive).
- All test cases contain valid one word strings.
"""
def is_isogram(word):
    word_to_check = word.upper()
    for i in word_to_check:
        count = 0
        for j in word_to_check:
            if i == j:
                count += 1
            if count > 1:
                return False
    return True

# print(is_isogram("Algorism"))

"""
Create a function that returns a base-2 (binary) representation of a base-10 (decimal) string number. To convert is simple: ((2) means base-2 and (10) means base-10) 010101001(2) = 1 + 8 + 32 + 128.
Going from right to left, the value of the most right bit is 1, now from that every bit to the left will be x2 the value, value of an 8 bit binary numbers are (256, 128, 64, 32, 16, 8, 4, 2, 1).
Notes:
- Numbers will always be below 1024 (not including 1024).
- The strings will always go to the length at which the most left bit's value gets bigger than the number in decimal.
- If a binary conversion for 0 is attempted, return "0".
"""
def binary(decimal):
    if decimal == 0:
        return "0"
    result = bin(decimal)
    return result.replace("0b", "")

# print(binary(123456))