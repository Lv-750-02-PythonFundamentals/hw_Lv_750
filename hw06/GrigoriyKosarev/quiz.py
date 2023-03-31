
"""
Given an unsorted list, create a function that returns the nth smallest integer (the smallest integer is the first smallest, the second smallest integer is the second smallest, etc).
Notes:
- n will always be >= 1.
- Each number in the array will be distinct (there will be a clear ordering).
- Given an out of bounds parameter (e.g. a list is of size k), and you are asked to find the m > k smallest integer, return None.
"""
from builtins import set


def nth_smallest(lst, n):
  if len(lst) < n:
    return None
  lst.sort()
  return lst[n-1]

# print(nth_smallest([5,2,6,8,3], 6))

"""
Create a function that takes a list and finds the list of integers that appear an odd number of times.
"""
def find_odd(lst):
  result = []
  set_lst = set(lst)
  for el in set_lst:
    if lst.count(el) % 2 != 0:
      result.append(el)
  return result

# print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5])) #[-1]
# print(find_odd([20, 1, 1, 2, 1, 2, 3, 3, 5, 5, 4, 20, 4, 5])) #[1, 5]
# print(find_odd([10])) #[10]

"""
Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
Notes:
- Zero is a non-negative integer.
- The given list only has integers and strings.
- Numbers in the list should not repeat.
- The original order must be maintained.
"""
def filter_list(lst):
  result = []
  for el in lst:
    if type(el) == str:
      continue
    if el >= 0:
      if result.count(el) == 0:
        result.append(el)
  return result

# print(filter_list([1,2,3,"123",2,-4,0]))

"""
Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. 
This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
"""
def add_indexes(lst):
  i = 0
  for el in lst:
    lst[i] = el + i
    i += 1
  return lst

# print(add_indexes([1, 1, 2]))
"""
Given a list of numbers and a value n, write a function that returns the probability of choosing a number greater than or equal to n from the list. 
The probability should be expressed as a percentage, rounded to one decimal place.
Notes. Precent probability of event = 100 * (num of favourable outcomes) / (total num of possible outcomes)
"""
def probability(lst, num):
    count_num = 0
    for el in lst:
      if el >= num:
        count_num += 1

    return round(100 * count_num / len(lst), 1)

print(probability([7, 4, 17, 14, 12, 3], 16)) #16.7