import unittest
from functions import greeting_by_name, get_symbol_position, merge


class TestFunctions(unittest.TestCase):

    def test_greeting_by_name(self):
        result = greeting_by_name("Pedro")
        self.assertEqual(result, "Hello Pedro!")

        result = greeting_by_name("")
        self.assertEqual(result, "Hello !")

    def test_get_symbol_position(self):
        text = "Hello Pedro"
        symbol = "o"
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, 5)

        symbol = "x"
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, "Not found")

        symbol = "xx"
        result = get_symbol_position(text, symbol)
        self.assertEqual(result, "Error! Symbol can be string with only one letter")

    def test_merge(self):
        dict1 = {'x': 1, 'y': 2}
        dict2 = {'y': 3, 'h': 4}
        result = merge(dict1, dict2)
        self.assertEqual(result, {'x': 1, 'y': 3, 'h': 4})

        dict1 = {}
        dict2 = {'x': 1, 'y': 2}
        result = merge(dict1, dict2)
        self.assertEqual(result, {'x': 1, 'y': 2})

        dict1 = {'x': 1, 'y': 2}
        dict2 = {}
        result = merge(dict1, dict2)
        self.assertEqual(result, {'x': 1, 'y': 2})


if __name__ == '__main__':
    unittest.main()