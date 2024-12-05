import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.calculator import (
    add, subtract, multiply, divide, factorial, 
    find_minimum, power, is_prime, gcd, average
)

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(1, 1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        with self.assertRaises(ValueError):
            divide(5, 0)

    def test_factorial(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(3.14)

    def test_find_minimum(self):
        self.assertEqual(find_minimum(5, 3), 3)
        self.assertEqual(find_minimum(-1, 1), -1)
        self.assertEqual(find_minimum(2.5, 2.5), 2.5)
        self.assertEqual(find_minimum(-10, -5), -10)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(-2, 3), -8)

    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
        with self.assertRaises(TypeError):
            is_prime(3.14)

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(54, 24), 6)
        self.assertEqual(gcd(7, 13), 1)
        self.assertEqual(gcd(0, 5), 5)
        with self.assertRaises(TypeError):
            gcd(3.14, 2)

    def test_average(self):
        self.assertEqual(average(1, 2, 3), 2)
        self.assertEqual(average(1), 1)
        self.assertEqual(average(-1, 1), 0)
        with self.assertRaises(ValueError):
            average()

if __name__ == '__main__':
    unittest.main() 