import unittest

from parameterized import parameterized

from leetcode.contest.bw17.bw17 import Solution, TreeNode


class TestBWC17(unittest.TestCase):


    def test_sumEvenGrandparent(self):
        root = TreeNode(2)
        node1 = TreeNode(1)
        node2 = TreeNode(1)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node1.left = node3
        node2.right = node4
        root.left = node1
        root.right = node2
        self.assertEqual(7, Solution().sumEvenGrandparent(root))

    @parameterized.expand([
        ['0', [1, 2, 3, 4], [2, 4, 4, 4]],
        ['1', [4, 2], [2, 2, 2, 2]],
    ])
    def test_decompressRLElist(self, name, nums, expected):
        self.assertEqual(expected, Solution().decompressRLElist(nums))

    @parameterized.expand([
        ['0', [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, [[12, 21, 16], [27, 45, 33], [24, 39, 28]]],
        ['1', [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, [[45, 45, 45], [45, 45, 45], [45, 45, 45]]],
        ['2', [[1, 2, 3], [4, 5, 6]], 0, [[1, 2, 3], [4, 5, 6]]]
    ])
    def test_matrixBlockSum(self, name, mat, K, expected):
        self.assertEqual(expected, Solution().matrixBlockSum(mat, K))

    # @parameterized.expand([
    #     ['0', "abcabcabc", 3],
    #     ['1', "leetcodeleetcode", 2],
    # ])
    # def test_distinctEchoSubstrings(self, name, text, expected):
    #     self.assertEqual(expected, Solution().distinctEchoSubstrings(text))
