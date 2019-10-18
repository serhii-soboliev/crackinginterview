import unittest

from parameterized import parameterized

from str.string import String


class TestString(unittest.TestCase):

    @parameterized.expand([
        ['character', "character", "carac"],
        ['civicw', "civicw", "civic"],
    ])
    def test_find_longest_palindrome_subsequence(self, name, in_str, expected):
        self.assertEqual(
            expected,
            String(in_str).find_longest_palindrome_subsequence(),
            "Failed to find longest palindrome subsequence for" + name)