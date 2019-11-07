import unittest

from parameterized import parameterized

from algo.codeforces.cr.n597.a_good_old_numbers_coloring import is_finite


class TestGoodOldNumbersColoring(unittest.TestCase):

    @parameterized.expand([
        ['1', 1, 1, True],
        ['2', 2, 4, False],
        ['3', 10, 10, False],
        ['4', 7, 3, True]
    ])
    def test_good_old_number_coloring(self, name, a, b, expected):
        self.assertEqual(expected, is_finite(a,b))


if __name__ == '__main__':
    unittest.main()
