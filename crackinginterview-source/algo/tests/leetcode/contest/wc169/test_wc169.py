import unittest

from parameterized import parameterized

from leetcode.contest.wc169.solution import Solution


class TestWC168(unittest.TestCase):

    @parameterized.expand([
        ['0', "aaaa", 1, 3, 3, 2],
        ['1', "aabcabcab", 2, 2, 3, 3]
    ])
    def test_max_freq(self, name, s, maxLetters, minSize, maxSize, expected):
        self.assertEqual(expected, Solution().method1())
