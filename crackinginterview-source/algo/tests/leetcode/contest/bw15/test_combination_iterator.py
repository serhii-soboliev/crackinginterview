import unittest

from leetcode.contest.bw15.CombinationIterator import CombinationIterator


class TestCombinationIterator(unittest.TestCase):

    def test_find_special_integer(self):
        ci = CombinationIterator("abc", 2)
        self.assertTrue(ci.hasNext())
        self.assertEqual(ci.next(), "ab")
        self.assertTrue(ci.hasNext())
        self.assertEqual(ci.next(), "ac")
        self.assertTrue(ci.hasNext())
        self.assertEqual(ci.next(), "bc")
        self.assertFalse(ci.hasNext())
