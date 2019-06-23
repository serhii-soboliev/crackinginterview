import unittest
from parameterized import parameterized
import numpy as np

from dynamic.tasks.longest_common_subsequence import LongestCommonSubSequence


class TestLongestCommonSubsequence(unittest.TestCase):

    def setUp(self):
        self.lcs = LongestCommonSubSequence()

    @parameterized.expand([
        ['1', 'abcbdab', 'bdcaba', 'bcba']
    ])
    def test_find_longest_subsequence(self, n, s1, s2, r):
        self.assertEqual(self.lcs.lcs(s1, s2), r)