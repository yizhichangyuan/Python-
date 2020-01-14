import unittest

from nameFunction import nameTest
class TestNameFunction(unittest.TestCase):
    def test_name1(self):
        name = nameTest('jam','bov','jd')
        self.assertEqual(name,"Jam Bov Jd")

    def test_name2(self):
        name = nameTest('jam','bov')
        self.assertEqual(name,"Jam Bov")

