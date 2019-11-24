import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_53_max_subarray import MaxSubArray


class TestMaxSubArray(unittest.TestCase):

    @parameterized.expand([
        ['0', [-2, 1, -3, 4, -1, 2, 1, -5, 4], 6],
        ['1', [], 0],
        ['2', [-1], -1],
        ['3', [1], 1]
    ])
    def test_max_sub_array(self, name, prices, expected):
        self.assertEqual(
            expected,
            MaxSubArray().max_subarray(prices),
            msg="MaxSubArray for test # {} must be {}".format(name, expected)
        )
