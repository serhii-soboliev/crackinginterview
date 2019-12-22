import unittest

from parameterized import parameterized

from leetcode.contest.wc167.wc167_ import Solution
from leetcode.contest.wc167.wc167_ import ListNode


class TestWC167(unittest.TestCase):

    @parameterized.expand([
        ['0', [
            [0, 0, 0],
            [1, 1, 0],
            [0, 0, 0],
            [0, 1, 1],
            [0, 0, 0]
        ], 1, 6],
        ['1', [
            [0, 1, 1],
            [1, 1, 1],
            [1, 0, 0]
        ], 1, -1],
        ['1', [
            [0, 1],
            [1, 1],
            [0, 0]],
         2, 3],
        ['3', [
            [0, 1, 1],
            [1, 1, 1],
            [1, 0, 0]
        ], 1, -1]
    ])
    def test_shortestPath(self, name, m, t, expected):
        self.assertEqual(expected, Solution().shortestPath(m, t))

    def test_getDecimalValue(self):
        l = ListNode(1, ListNode(0, ListNode(1, None)))
        self.assertEqual(5, Solution().getDecimalValue(l))

    @parameterized.expand([
        ['0', 100, 300, [123, 234]],
        ['1', 1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]]
    ])
    def test_sequentialDigits(self, name, low, high, expected):
        self.assertEqual(expected, Solution().sequentialDigits(low, high))

    @parameterized.expand([
        ['0', [
            [1, 1, 3, 2, 4, 3, 2],
            [1, 1, 3, 2, 4, 3, 2],
            [1, 1, 3, 2, 4, 3, 2]
        ], 4, 2],
        ['1', [
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2]
        ], 1, 0],
        ['2', [
            [1, 1, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
            [1, 0, 0, 0]
        ], 6, 3],
        ['3', [
            [18, 70],
            [61, 1],
            [25, 85],
            [14, 40],
            [11, 96],
            [97, 96],
            [63, 45]
        ], 40184, 2],
    ])
    def test_sequentialDigits(self, name, m, t, expected):
        self.assertEqual(expected, Solution().maxSideLength(m, t))
