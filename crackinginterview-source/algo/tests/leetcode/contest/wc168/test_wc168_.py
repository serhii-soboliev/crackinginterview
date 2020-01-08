import unittest

from parameterized import parameterized

from leetcode.contest.wc168.wc168_ import Solution


class TestWC168(unittest.TestCase):

    @parameterized.expand([
        ['0', [1, 0, 1, 0],
              [7, 5, 4, 100],
              [[], [], [1], []],
              [[1, 2], [3], [], []],
              [0], 16],
        ['1', [1, 0, 0, 0, 0, 0],
              [1, 1, 1, 1, 1, 1],
              [[1, 2, 3, 4, 5], [], [], [], [], []],
              [[1, 2, 3, 4, 5], [], [], [], [], []],
               [0], 6],
        ['2', [1, 1, 1],
              [100, 1, 100],
              [[], [0, 2], []],
              [[], [], []],
              [1], 1],
        ['3', [1], [100], [[]], [[]], [], 0],
        ['4', [1, 1, 1], [2, 3, 2], [[], [], []], [[], [], []], [2, 1, 0], 7]
    ])
    def test_max_candies(self, name, status, candies, keys, containedBoxes, initialBoxes, expected):
        self.assertEqual(expected, Solution().max_candies(status, candies, keys, containedBoxes, initialBoxes))

    @parameterized.expand([
        ['0', "aaaa", 1, 3, 3, 2],
        ['1', "aabcabcab", 2, 2, 3, 3]
    ])
    def test_max_freq(self, name, s, maxLetters, minSize, maxSize, expected):
        self.assertEqual(expected, Solution().maxFreq(s, maxLetters, minSize, maxSize))

    @parameterized.expand([
        ['0', [1, 2, 3, 3, 4, 4, 5, 6], 4, True],
        ['0', [3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3, True],
    ])
    def test_sequentialDigits(self, name, nums, k, expected):
        self.assertEqual(expected, Solution().isPossibleDivide(nums, k))

    @parameterized.expand([
        ['0', "{[]}", True]
    ])
    def test_isvalid(self, name, s, expected):
        self.assertEqual(expected, Solution().isValid(s))
