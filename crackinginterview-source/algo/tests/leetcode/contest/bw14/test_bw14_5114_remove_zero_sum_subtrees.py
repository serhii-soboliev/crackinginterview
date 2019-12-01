import unittest

from parameterized import parameterized

from leetcode.contest.bw14.bw14_5114_remove_zero_sum_subtrees import RemoveZeroSumSubtrees


class TestRemoveSubtrees(unittest.TestCase):

    @parameterized.expand([
        ['0', 7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -1], 2],
        ['1', 7, [-1, 0, 0, 1, 2, 2, 2], [1, -2, 4, 0, -2, -1, -2], 6],
        ['2', 5, [-1, 0, 1, 0, 0], [-672, 441, 18, 728, 378], 5],
    ])
    def test_remove_zero_subtrees(self, name, nodes, parent, value, expected):
        self.assertEqual(expected, RemoveZeroSumSubtrees().delete_tree_nodes(nodes, parent, value))
