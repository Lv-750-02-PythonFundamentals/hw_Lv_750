from heapq import merge
import unittest

from functions import get_symbol_position, greeting_by_name, merge
# uncomment next line if you want to run tests with errors
# from functions_with_errors import get_symbol_position, greeting_by_name, merge

class FunctionsTests(unittest.TestCase):

    def test_greeting_by_name(self):
        name = "Ketryin"
        self.assertEqual(greeting_by_name(name), "Hello Ketryin!")

    def test_get_symbol_position(self):
        text = "Hello!"
        symbol = "o"
        self.assertEqual(get_symbol_position(text, symbol), 5)

    def test_get_symbol_position_wrong_symbol(self):
        text = "Hello World!"
        symbol = "x"
        self.assertEqual(get_symbol_position(text, symbol), "Not found")

    def test_get_symbol_position_wrong_string(self):
        text = "Hello World!"
        symbol = "aa"
        self.assertEqual(get_symbol_position(text, symbol), 'Error! Symbol can be string with only one letter')

    def test_merge(self):  
        dict1 = {"1": 1, "2": 2}
        dict2 = {"3": 3}
        new_dict = merge(dict1, dict2)
        self.assertEqual(new_dict, {"1": 1, "2": 2, "3": 3})


if __name__ == '__main__':
    unittest.main()