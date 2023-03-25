import unittest

from func import div


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print("\tsetUp")

    def tearDown(self):
        print("\ttearDown")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def test_error(self):
        print("\t\ttest test_error")
        actual = div(1, 0)
        self.assertEqual(actual, "error")

    def test_error_fail(self):
        print("\t\ttest test_error")
        actual = div(1, 0)
        self.assertEqual(actual, "qerror")

    # def test_equal(self):
    #     print("\t\ttest test_error_fail")
    #     actual = div(1, 1)
    #     self.assertEqual(actual, -1)

    def test_div(self):
        print("\t\ttest test_error_fail")
        actual = div(1, 2)
        self.assertEqual(actual, 0.5)

a = "aaaa"