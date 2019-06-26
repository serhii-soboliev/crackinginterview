import unittest
from parameterized import parameterized
import numpy as np

from dynamic.tasks.longest_common_subsequence import LongestCommonSubSequence


class TestLongestCommonSubsequence(unittest.TestCase):

    def setUp(self):
        self.lcs = LongestCommonSubSequence()

    @parameterized.expand([
        ['1', 'abcbdab', 'bdcaba', 'bdab']
    ])
    def test_find_longest_subsequence_rec(self, n, s1, s2, r):
        self.assertEqual(self.lcs.lcs_recursive(s1, s2), r)

    @parameterized.expand([
        ['1', 'abcbdab', 'bdcaba', 'bcba'],
        ['2', 'abACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA', 'GTCGTCGGAAGCCGGCCGAA'],
        ['3', '10010101', '010110110', '100110'],
    ])
    def test_find_longest_subsequence(self, n, s1, s2, r):
        self.assertEqual(self.lcs.lcs(s1, s2), r)

    @parameterized.expand([
        ['1', 'abcbdab', 'bdcaba', 'bcba'],
        ['2', 'abACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA', 'GTCGTCGGAAGCCGGCCGAA'],
        ['3', '10010101', '010110110', '100110'],
    ])
    def test_find_longest_subsequence_dict(self, n, s1, s2, r):
        self.assertEqual(self.lcs.lcs_dict(s1, s2), r)
