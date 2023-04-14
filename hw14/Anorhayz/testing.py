import unittest
from functions import greeting_by_name, get_symbol_position, merge


class FunctionTesting(unittest.TestCase):
    def test_greeting_by_name(self):
        some_name = "Donald"
        self.assertEqual(greeting_by_name(some_name), "Hello Donald!")

    def test_get_symbol_position_wrong_symbol(self):
        test_text = "Hello there"
        test_symbol = "y"
        self.assertEqual(get_symbol_position(test_text, test_symbol), "Not found")

    def test_get_symbol_position(self):
        test_text = "Python"
        test_symbol = "h"
        self.assertEqual(get_symbol_position(test_text, test_symbol), 4)

    def test_get_symbol_position_symbol_check(self):
        test_text = "Hello world"
        test_symbol = "ll"
        self.assertEqual(get_symbol_position(test_text, test_symbol),
                         "Error! Symbol can be string with only one letter")

    def test_merge(self):
        test_dict1 = {"test1": 5, "test2": 9}
        test_dict2 = {"test3": 6}
        test_new_dict = merge(test_dict1, test_dict2)
        self.assertEqual(test_new_dict, {"test1": 5, "test2": 9, "test3": 6})


if __name__ == "__main__":
    unittest.main()
