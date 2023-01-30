import unittest

from people_in_the_bus import people_in_the_bus, pay_stop

in_out_1 = [10, 0]
in_out_2 = [3, 5]

class MyTestCase(unittest.TestCase):
    def test_pay_stop(self):
        self.assertEqual(pay_stop(in_out_1), 10)
        self.assertEqual(pay_stop(in_out_2), -2)

    def test_people_in_the_bus(self):
        self.assertEqual(people_in_the_bus([[10,0],[3,5],[5,8]]),5)
        self.assertEqual(people_in_the_bus([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
        self.assertEqual(people_in_the_bus([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)


if __name__ == '__main__':
    unittest.main()
