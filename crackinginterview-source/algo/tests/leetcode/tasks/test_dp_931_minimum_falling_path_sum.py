import unittest

from parameterized import parameterized

from leetcode.tasks.dp_931_minimum_falling_path_sum import MinFallingPathSum


class TestMinFallingPathSum(unittest.TestCase):

    @parameterized.expand([
        ['0', [[1,2,3],[4,5,6],[7,8,9]], 12]
    ])
    def test_min_falling_path_sum(self, name, a, expected):
        self.assertEqual(MinFallingPathSum().min_falling_path_sum(a), expected)


if __name__ == '__main__':
    unittest.main()
