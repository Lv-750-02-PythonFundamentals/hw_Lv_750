def count_chars(string):
    count = {}

    for char in string:
        if char not in count:
            count[char] = 1
        else:
            count[char] += 1 
    return count

string = input("Enter your string to count characters in it: ")
print(count_chars(string))
