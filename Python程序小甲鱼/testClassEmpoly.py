import unittest

from Empoy import Employee

class testEmpoly(unittest.TestCase):
    def setUp(self):
        self.empoly = Employee('Jun','He',20000)

    def test_give_default_raise(self):
        self.empoly.give_raise()
        self.assertEqual(self.empoly.annualSalary,25000)

    def test_give_custom_arise(self):
        self.empoly.give_raise(10000)
        self.assertEqual(self.empoly.annualSalary,30000)
