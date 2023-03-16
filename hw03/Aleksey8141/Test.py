# def mean(num):
#     digits = [int(d) for d in str(num) if d != '0']
#     return sum(digits) // len(digits)
# print(mean(1204))

# def is_isogram(word):
#     word = word.lower()
#     for char in word:
#         if word.count(char) > 1:
#             return False
#     return True
#
#     return

# def integer_boolean(binary_number):
#     return [digit == "1" for digit in binary_number]

# def count_vowels(word):
#     vowels = 'aeiou'
#     count = 0
#     for char in word:
#         if char.lower() in vowels:
#             count += 1
#     return count

# def binary(decimal):
#     if decimal == 0:
#         return "0"
#     binary = ""
#     while decimal > 0:
#         binary = str(decimal % 2) + binary
#         decimal //= 2
#     return binary



# def probability(lst, num):
#     count = len([x for x in lst if x >= num])
#     total = len(lst)
#     return round(100 * count / total, 1)

# def find_odd(lst):
#     counts = {}
#     for num in lst:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1
#     result = []
#     for num, count in counts.items():
#         if count % 2 != 0:
#             result.append(num)
#     return result

# def add_indexes(lst):
#     return [num + i for i, num in enumerate(lst)]

# def filter_list(lst):
#     return [x for x in lst if type(x) == int]

# def nth_smallest(lst, n):
#     if n > len(lst):
#         return None
#     sorted_lst = sorted(lst)
#     return sorted_lst[n-1]

from math import*

def reverse(st):
    words = st.split()
    words.reverse()
    reversed_string = ' '.join(words)
    print (reversed_string)
reverse('Hello World.')


