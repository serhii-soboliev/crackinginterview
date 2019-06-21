import unittest
from parameterized import parameterized
import numpy as np

from dynamic.tasks.matrix_multiply import MatrixMultiply


class TestMatrixMultiply(unittest.TestCase):

    def test_simple_matrix_multiply_with_invalid_shapes(self):
        a = [
            [1, 2, 3],
            [1, 2, 3]
        ]
        b = [
            [1, 2],
            [1, 2]
        ]
        with self.assertRaisesRegexp(AssertionError,
                                     'Number of matrix A columns should be equal to number of matrix B rows'):
            MatrixMultiply.simple_matrix_multiply(a, b)

    def test_simple_matrix_multiply_random(self):
        n = 3
        m = 7
        l = 9
        a = np.random.rand(n, l)
        b = np.random.rand(l, m)
        np.testing.assert_array_almost_equal(
            np.dot(a, b),
            MatrixMultiply.simple_matrix_multiply(a, b)
        )

    @parameterized.expand([
        ['1', [10, 100, 5, 50], 7500],
        ['2', [30, 35, 15, 5, 10, 20, 25], 15125]
    ])
    def test_matrix_minimum_multiplications_recursion(self, name, dimensions, count):
        self.assertEqual(
            MatrixMultiply.count_minimum_multiplications_recursion(dimensions),
            count
        )

    @parameterized.expand([
        ['1', [10, 100, 5, 50], 7500, "((A0A1)A2)"],
        ['2', [30, 35, 15, 5, 10, 20, 25], 15125, "((A0(A1A2))((A3A4)A5))"]
    ])
    def test_matrix_minimum_multiplications(self, name, dimensions, expected_count, expected_parens):
        count, parens = MatrixMultiply.count_minimum_multiplications(dimensions)
        self.assertEqual(count, expected_count)
        self.assertEqual(parens, expected_parens)