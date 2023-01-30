import unittest

from people_in_the_bus import people_in_the_bus


class MyTestCase(unittest.TestCase):
    def test_people_in_the_bus(self):
        self.assertEqual(people_in_the_bus([[10,0],[3,5],[5,8]]),5)
        self.assertEqual(people_in_the_bus([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]]),17)
        self.assertEqual(people_in_the_bus([[3,0],[9,1],[4,8],[12,2],[6,1],[7,8]]),21)


if __name__ == '__main__':
    unittest.main()
