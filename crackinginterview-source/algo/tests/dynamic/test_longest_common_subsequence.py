import unittest

from parameterized import parameterized

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
        ['4', '', '', ''],
    ])
    def test_find_longest_subsequence(self, n, s1, s2, r):
        self.assertEqual(self.lcs.lcs(s1, s2), r)

    @parameterized.expand([
        ['1', 'abcbdab', 'bdcaba', 'bcba'],
        ['2', 'abACCGGTCGAGTGCGCGGAAGCCGGCCGAA', 'GTCGTTCGGAATGCCGTTGCTCTGTAAA', 'GTCGTCGGAAGCCGGCCGAA'],
        ['3', '10010101', '010110110', '100110'],
        ['4', '', '', ''],
        ['5', '', 'a', ''],
        ['6', 'a', '', '']
    ])
    def test_find_longest_subsequence_dict(self, n, s1, s2, r):
        self.assertEqual(self.lcs.lcs_dict(s1, s2), r)


    @parameterized.expand([
        ['1', 'abca', ['abc']],
        ['1', 'ba', ['a','b']],
        ['2', '', ['']],
        ['3', 'cbdbf', ['bdf','cdf']],
        ['4', 'wladbce', ['abce']],
    ])
    def test_increasing_lcs(self,n,s,r):
        self.assertEqual(r, self.lcs.lis(s))
