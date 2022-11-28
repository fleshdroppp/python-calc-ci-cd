import unittest
from main import Calculator

#Calculator Tests

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 6), 8)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(8, 7), 56)

    def test_substract(self):
        self.assertEqual(self.calculator.substract(-3, 7), -10)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(2, 10), 0.2)


unittest.main()

