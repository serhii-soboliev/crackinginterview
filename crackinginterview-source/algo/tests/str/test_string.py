import unittest

from parameterized import parameterized

from str.string import String


class TestString(unittest.TestCase):

    @parameterized.expand([
        ['carac', "character", "carac"],
        ['civic', "civicw", "civic"],
        ['BABCBAB', "BBABCBCAB", "BABCBAB"],
        ['sullus', "wswwuiollust", "sullus"],
    ])
    def test_find_longest_palindrome_subsequence_using_reverse(self, name, in_str, expected):
        self.assertEqual(
            expected,
            String(in_str).find_longest_palindrome_subsequence_using_reverse(),
            "Longest palindrome subsequence for {} should be {} ".format(in_str, expected)
        )

    @parameterized.expand([
        ['carac', "character", "carac"],
        ['civic', "civicw", "civic"],
        ['BABCBAB', "BBABCBCAB", "BACBCAB"],
        ['sullus', "wswwuiollust", "sullus"],
    ])
    def test_find_longest_palindrome_subsequence(self, name, in_str, expected):
        self.assertEqual(
            expected,
            String(in_str).find_longest_palindrome_subsequence_length(),
            "Longest palindrome subsequence for {} should be {} ".format(in_str, expected)
        )

    @parameterized.expand([
        ['1', "abc", "ahbgdc", True],
        ['2', "axc", "ahbgdc", False],
        ['3', "", "ahbgdc", True]
    ])
    def test_is_subsequence(self, name, s, t, expected):
        self.assertEqual(expected,
                         String("").is_subsequence(s, t),
                         "Test #{}.{} is substring for {}".format(name, s, t) if expected else "{} is substring for {}".format(name, s, t))