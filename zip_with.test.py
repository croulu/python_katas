import unittest

from zip_with import zip_with, add, sub, mul


class MyTestCase(unittest.TestCase):
    def test_basics(self):
        self.assertEqual(zip_with(add, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1]), [6, 6, 6, 6, 6, 6])
        self.assertEqual(zip_with(add, [0, 1, 2, 3, 4], [6, 5, 4, 3, 2, 1]), [6, 6, 6, 6, 6])
        self.assertEqual(zip_with(add, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2]), [6, 6, 6, 6, 6])
        self.assertEqual(zip_with(pow, [10, 10, 10, 10], [0, 1, 2, 3]), [1, 10, 100, 1000])
        self.assertEqual(zip_with(max, [1, 4, 7, 1, 4, 7], [4, 7, 1, 4, 7, 1]), [4, 7, 7, 4, 7, 7])
        self.assertEqual(zip_with(add, [0, 1, 2, 3], [0, 1, 2, 3]), [0, 2, 4, 6])
        self.assertEqual(zip_with(add, [0, 1, 2, 3], [0, 1, 2, 3]), [0, 2, 4, 6])
        self.assertEqual(zip_with(pow, [10, 10, 10, 10, 10, 10, 10], [0, 1, 2, 3, 4, 5, 6]), [1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6])
        self.assertEqual(zip_with(sub, [0, 1, 2, 3, 4, 5], [6, 5, 4, 3, 2, 1]), [-6, -4, -2, 0, 2, 4])
        self.assertEqual(zip_with(mul, ["a", "b", "c", "d", "e", "f"], [6, 5, 4, 3, 2, 1]), ["aaaaaa", "bbbbb", "cccc", "ddd", "ee", "f"])


if __name__ == '__main__':
    unittest.main()
