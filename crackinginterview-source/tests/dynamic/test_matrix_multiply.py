import unittest
import parameterized
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

    def test_simple_matrix_multiply(self):
        a = [
                [1,2,3],
                [1,2,3]
        ]
        b = [
                [1,2,3,4],
                [1,2,3,4],
                [1,2,3,4]
        ]
        r = MatrixMultiply.simple_matrix_multiply(a,b)
        self.assertEqual(np.shape(r), (2,4))