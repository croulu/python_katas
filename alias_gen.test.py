import unittest

from alias_gen import alias_gen, first_letter_in_uppercase, find_alias, FIRST_NAME, SURNAME, map_complete_name

basic_tests = (
    (('Mike', 'Millington'), 'Malware Mike')
)

aabasic_tests = (
    (('Mike', 'Millington'), 'Malware Mike'),
    (('Fahima', 'Tash'), 'Function T-Rex'),
    (('Daisy', 'Petrovic'), 'Data Payload'),
    (('Barny', 'White'), 'Beta Worm'),
    (('Hank', 'Kutz'), 'Half-life Killer'),
    (('123abc', 'Pinkman'), 'Your name must start with a letter from A - Z.'),
    (('walter', 'white'), 'WiFi Worm')
)

name_a = 'alfred'
letter_a = 'A'

name_1 = '123 alfred'
letter_1 = 'NotAStr'

to_find_first_name = 'cosy'
to_find_last_name = 'tony'
alias_found_complete = 'Cache T-Rex'

class MyTestCase(unittest.TestCase):

    def test_first_letter(self):
        self.assertEqual(first_letter_in_uppercase(name_a), letter_a)
        self.assertEqual(first_letter_in_uppercase(name_1), letter_1)

    def test_find_alias(self):
        self.assertEqual(map_complete_name(to_find_first_name, to_find_last_name), alias_found_complete)

    def test_something(self):
        for names, result in basic_tests:
            self.assertEqual(alias_gen(*names), result)


if __name__ == '__main__':
    unittest.main()
