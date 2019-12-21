import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_413_arithmetic_slices import number_of_arithmetic_slices


class TestArithmeticSlices(unittest.TestCase):

    @parameterized.expand([
        ['0', [1, 2, 3, 4], 3]
    ])
    def test_number_of_arithmetic_slices(self, name, a, expected):
        self.assertEqual(number_of_arithmetic_slices(a), expected)


if __name__ == '__main__':
    unittest.main()