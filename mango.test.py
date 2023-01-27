import unittest

from mango import mango, offer_how_much, pay_how_much

DEAL1 = 4
OFFER_FOR_DEAL1 = 1
PAY_FOR_DEAL1 = 3

DEAL2 = 9
OFFER_FOR_DEAL2 = 3
PAY_FOR_DEAL2 = 6


class MyTestCase(unittest.TestCase):

    # @unittest.skip("pas fini")
    def test_mango(self):
        self.assertEqual(mango(3, 3), 6)
        self.assertEqual(mango(9, 5), 30)

    def test_offer_how_much(self):
        self.assertEqual(offer_how_much(DEAL1), OFFER_FOR_DEAL1)
        self.assertEqual(offer_how_much(DEAL2), OFFER_FOR_DEAL2)

    def test_pay_how_much(self):
        self.assertEqual(pay_how_much(DEAL1), PAY_FOR_DEAL1)
        self.assertEqual(pay_how_much(DEAL2), PAY_FOR_DEAL2)


if __name__ == '__main__':
    unittest.main()
