import unittest
from square_roots import get_square_roots


class TestSqrtFunction(unittest.TestCase):
    def test_a_is_zero(self):
        result = get_square_roots(0, 8, 16)
        self.assertIsInstance(result, float)
        self.assertEqual(result, -2)

    def test_a_is_zero_b_is_zero(self):
        result = get_square_roots(0, 0, 8)
        self.assertIsNone(result)

    def test_b_is_zero_c_negative(self):
        result = get_square_roots(2, 0, -32)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], -4)
        self.assertEqual(result[1], 4)

    def test_b_is_zero_c_is_zero(self):
        result = get_square_roots(123, 0, 0)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 0)

    def test_b_is_zero_c_positive(self):
        result = get_square_roots(3, 0, 9)
        self.assertIsNone(result)

    def test_c_is_zero(self):
        result = get_square_roots(3, 6, 0)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], -2)

    def test_all_zero(self):
        result = get_square_roots(0, 0, 0)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "Бесконечность")

    def test_d_greater_than_zero(self):
        result = get_square_roots(4, -12, 5)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], 0.5)
        self.assertAlmostEqual(result[1], 2.5)

        result_2 = get_square_roots(6, 11, -10)
        self.assertIsInstance(result_2, list)
        self.assertEqual(len(result_2), 2)
        self.assertEqual(result_2[0], -2.5)
        self.assertAlmostEqual(result_2[1], 0.6667, 4)

    def test_d_lower_than_zero(self):
        result = get_square_roots(20, -2, 3)
        self.assertIsNone(result)

    def test_d_is_zero(self):
        result = get_square_roots(4, 8, 4)
        self.assertIsInstance(result, float)
        self.assertEqual(result, -1)
