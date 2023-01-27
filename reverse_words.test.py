import unittest

from reverse_words import reverse_words

WORD_1 = 'bonjour tout le monde !'
WORD_1_REVERSE = '! ednom el tuot ruojnob'


class MyTestCase(unittest.TestCase):

    def test_reverse_words(self):
        self.assertEqual(reverse_words(WORD_1), WORD_1_REVERSE)


if __name__ == '__main__':
    unittest.main()
