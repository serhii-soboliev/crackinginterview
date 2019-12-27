import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_1143_longest_common_subsequence import LongestCommonSubsequence


class TestLongestCommonSubsequence(unittest.TestCase):

    @parameterized.expand([
        ['0', "abcde", "ace", 3],
        ['1', "abc", "abc", 3],
        ['2', "abc", "def", 0]
    ])
    def test_longest_common_subsequence_rec(self, name, text1, text2 , expected):
        self.assertEqual(LongestCommonSubsequence().longest_common_subsequence_rec(text1, text2), expected)

    @parameterized.expand([
        ['0', "abcde", "ace", 3],
        ['1', "abc", "abc", 3],
        ['2', "abc", "def", 0],
        ['3', "ylqpejqbalahwr", "yrkzavgdmdgtqpg", 3]
    ])
    def test_longest_common_subsequence(self, name, text1, text2, expected):
        self.assertEqual(LongestCommonSubsequence().longest_common_subsequence(text1, text2), expected)