import math
from builtins import print


def card_hide(card):
   if len(card) < 16:
       return "Invalid card"
   last4 = card[-4:]
   symbol_star = "*"*(len(card)-4)
   return f'{symbol_star}{last4}'


def return_negative(number):
    if number > 0:
        return -1 * number
    return number

# Write a function that returns True if k^k == n for input (n, k) and return False otherwise.
# The ^ operator refers to exponentiation operation **, not the bitwise XOR operation.
def k_to_k(num1, num2):
    if num2**num2 == num1:
        return True
    return False


def makes10(num1, num2):
    if type(num1) != int or type(num2) != int:
        return False
    if int(num1) == 10 or num2 == 10 or (num1 + num2) == 10:
       return True
    return False


def stutter(word):
    if len(word) < 2:
        return "oh..."
    return f"{word[0:2]}...{word[0:2]}...{word}"


def X_O(word):
    count_x = word.casefold().count("x")
    count_o = word.casefold().count("o")

    if (count_x + count_o) == 0:
        return True
    if count_x == count_o:
        return True
    else:
        return False


# print(card_hide("1234567891234567"))
# print(return_negative(12))
# print(k_to_k(4,2))
# print(makes10(2, 10))
# print(stutter("incredible"))

print(X_O("xooxx"))

print(math.factorial(3))