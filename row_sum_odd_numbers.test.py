import unittest

from row_sum_odd_numbers import say_odd, create_odds_for_me, sum_elements, row_sum_odd_numbers

odds_for_2 = [3, 5]
odds_for_3 = [7, 9, 11]
odds_for_5 = [21, 23, 25, 27, 29]


class MyTestCase(unittest.TestCase):

    def test_even_or_odd(self):
        self.assertEqual(say_odd(1), True)
        self.assertEqual(say_odd(2), False)
        self.assertEqual(say_odd(5), True)
        self.assertEqual(say_odd(10), False)

    def test_odds_for_me_and_previous(self):
        self.assertEqual(create_odds_for_me(2), odds_for_2)
        self.assertEqual(create_odds_for_me(3), odds_for_3)
        self.assertEqual(create_odds_for_me(5), odds_for_5)

    def test_sum_all(self):
        self.assertEqual(sum_elements(odds_for_2), 8)
        self.assertEqual(sum_elements(odds_for_3), 27)

    def test_basic_test_cases(self):
        self.assertEqual(row_sum_odd_numbers(1), 1)
        self.assertEqual(row_sum_odd_numbers(2), 8)
        self.assertEqual(row_sum_odd_numbers(13), 2197)
        self.assertEqual(row_sum_odd_numbers(19), 6859)
        self.assertEqual(row_sum_odd_numbers(41), 68921)


if __name__ == '__main__':
    unittest.main()
