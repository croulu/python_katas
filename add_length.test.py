import unittest

from add_length import add_length


class MyTestCase(unittest.TestCase):

    def test_add_length(self):
        self.assertEqual(add_length('apple ban'),["apple 5", "ban 3"])
        self.assertEqual(add_length('you will win'),["you 3", "will 4", "win 3"])
        self.assertEqual(add_length('you'),["you 3"])
        self.assertEqual(add_length('y'),["y 1"])


if __name__ == '__main__':
    unittest.main()
