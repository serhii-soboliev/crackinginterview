import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_1048_longest_string_chain import is_predecessor


class TestLongestStringChain(unittest.TestCase):

    @parameterized.expand([
        ['0', "ab", "abc", True],
        ['1', "ab", "aab", True],
        ['1', "ab", "acb", True],
        ['3', "ab", "acc", False],
        ['4', "", "a", True],
        ['5', "", "ab", False],
        ['6', "rew", "arew", True],
    ])
    def test_longest_arithmetic_sequence(self, name, a, b, expected):
        self.assertEqual(expected, is_predecessor(a, b))
