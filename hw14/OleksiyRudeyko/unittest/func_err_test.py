import unittest
from functions_with_errors import greeting_by_name, get_symbol_position, merge

class TestFunctions(unittest.TestCase):
    
    def test_greeting_by_name(self):
        name = "Alice"
        self.assertEqual(greeting_by_name(name), "Hello Alice!")
        
    def test_get_symbol_position(self):
        text = "Hello World!"
        symbol = "o"
        self.assertEqual(get_symbol_position(text, symbol), 5)

    def test_get_symbol_position_wrong_symbol(self):
        text = "Hello World!"
        symbol = "z"
        self.assertEqual(get_symbol_position(text, symbol), "Not found")
    
    def test_get_symbol_position_wrong_string(self):
        text = "Hello World!"
        symbol = "oo"
        self.assertEqual(get_symbol_position(text, symbol), 1)
        
    def test_merge1(self):  
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        new_dict = merge(dict1, dict2)
        self.assertEqual(new_dict, {"a": 1, "b": 2, "c": 3, "d": 4})
    
    def test_merge2(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        new_dict = merge(dict1, dict2)
        self.assertEqual(dict1, {"a": 1, "b": 2})
    
    def test_merge3(self):
        dict1 = {"a": 1, "b": 2}
        dict2 = {"c": 3, "d": 4}
        new_dict = merge(dict1, dict2)
        self.assertEqual(dict2, {"c": 3, "d": 4})

if __name__ == '__main__':
    unittest.main()
