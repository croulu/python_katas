import unittest

from row_sum_odd_numbers import row_sum_odd_numbers


class MyTestCase(unittest.TestCase):
    def basic_test_cases(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)
        self.assertEqual(row_sum_odd_numbers(2), 8)
        self.assertEqual(row_sum_odd_numbers(13), 2197)
        self.assertEqual(row_sum_odd_numbers(19), 6859)
        self.assertEqual(row_sum_odd_numbers(41), 68921)


if __name__ == '__main__':
    unittest.main()
