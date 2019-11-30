import unittest
from parameterized import parameterized

from codeforces.cr.n598.d_binary_string_minimizing import minimize_binary


class TestMinimizeBinary(unittest.TestCase):

    @parameterized.expand([
       # ['1', 10, 12, '0110111000', '0000111110'],
        ['2', 10, 17, '1100100100', '0000010111']
    ])
    def test_minimize_binary(self, name, n, k, s, expected):
        self.assertEqual(
            minimize_binary(n,k,s),
            expected
        )