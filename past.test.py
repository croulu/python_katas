import unittest

from past import past, sec_in_msec, min_in_sec, hou_in_min, hou_in_sec


class MyTestCase(unittest.TestCase):

    def test_past(self):
        self.assertEqual(past(0,1,1),61000)
        self.assertEqual(past(1,1,1),3661000)
        self.assertEqual(past(0,0,0),0)
        self.assertEqual(past(1,0,1),3601000)
        self.assertEqual(past(1,0,0),3600000)

    def test_sec_in_msec(self):
        self.assertEqual(sec_in_msec(1),1000)

    def test_min_in_sec(self):
        self.assertEqual(min_in_sec(1),60)

    def test_hou_in_min(self):
        self.assertEqual(hou_in_min(1),60)

    def test_hou_in_sec(self):
        self.assertEqual(hou_in_sec(1),3600)


if __name__ == '__main__':
    unittest.main()
