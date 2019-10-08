import unittest
from parameterized import parameterized

from codeforces.cr.n590.c_pipes import is_water_flow_possible


class TestPipes(unittest.TestCase):

    @parameterized.expand([
        ['1', 7, '2323216', '1615124', True],
        ['2', 1, '3', '4', True],
        ['3', 2, '13', '24', True],
        ['4', 2, '12', '34', False],
        ['5', 3, '536', '345', True],
        ['6', 2, '46', '56', False],
    ])
    def test_pipes(self, name,  n, a, b, expected):
        self.assertEqual(
            is_water_flow_possible(n, a, b),
            expected
        )
