import unittest
from main3 import remainder


class TestRemainderFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(10, 5), 0)
        self.assertEqual(remainder(15, 4), 3)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), 2)
        self.assertEqual(remainder(10, -3), -2)
        self.assertEqual(remainder(-10, -3), -1)

    def test_zero_numerator(self):
        self.assertEqual(remainder(0, 5), 0)
        self.assertEqual(remainder(0, -5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)

    def test_large_numbers(self):
        self.assertEqual(remainder(1000000, 3), 1)
        self.assertEqual(remainder(123456789, 10), 9)


if __name__ == '__main__':
    unittest.main()
