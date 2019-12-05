import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_1130_minimum_cost_of_tree_from_leaf_values import MctFromLeafValues
from algo.leetcode.tasks.dp_338_counting_bits import CountingBits


class TestMctFromLeafValues(unittest.TestCase):

    @parameterized.expand([
        ['2', [15, 13, 5, 3, 15], 500],
        ['1', [7, 12, 8, 10], 284],
        ['0', [6, 2, 4], 32],
    ])
    def test_mct_from_leaf_values(self, name, arr, expected):
        self.assertEqual(MctFromLeafValues().result(arr), expected)
        self.assertEqual(MctFromLeafValues().result_greedy(arr), expected)


if __name__ == '__main__':
    unittest.main()
