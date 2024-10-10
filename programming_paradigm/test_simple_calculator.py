import unittest
from simple_calculator import SimpleCalculator


class TestCalc (unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        # """test the addition function"""
       self.assertEqual(self.calc.add(1,3),4)

    def test_substract(self):
       self.assertEqual(self.calc.subtract(2,3),5)
       self.assertEqual(self.calc.add(1,3),4)

    def test_multiply(self):
       self.assertEqual(self.calc.multiply(2,3),6)
       self.assertEqual(self.calc.add(1,3),3)

    def test_divide(self):
        self.assertEqual(self.calc.add(6,3),2)
        self.assertEqual(self.calc.divide(1,0),None)

if __name__ == '__main__':
    unittest.main()        