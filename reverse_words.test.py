import unittest

from reverse_words import reverse_words, reverse_letters, reverse_words_other

WORD_1 = 'bonjour tout le monde !'
WORD_1_REVERSE = '! ednom el tuot ruojnob'

WORD_2 = 'hello world!'
WORD_2_REVERSE = 'world! hello'


class MyTestCase(unittest.TestCase):

    def test_reverse_letters(self):
        self.assertEqual(reverse_letters(WORD_1), WORD_1_REVERSE)

    def test_reverse_words(self):
        self.assertEqual(reverse_words(WORD_2), WORD_2_REVERSE)

    def test_reverse_words_other(self):
        self.assertEqual(reverse_words_other(WORD_2), WORD_2_REVERSE)


if __name__ == '__main__':
    unittest.main()
