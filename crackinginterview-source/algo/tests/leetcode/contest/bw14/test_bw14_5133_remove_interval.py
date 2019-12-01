import unittest

from parameterized import parameterized

from leetcode.contest.bw14.bw14_5133_remove_interval import RemoveInterval


class TestRemoveInterval(unittest.TestCase):

    @parameterized.expand([
        ['0', [[0,2],[3,4],[5,7]], [1,6], [[0,1],[6,7]]],
        ['1', [[0,5]], [2,3], [[0,2],[3,5]]]
    ])
    def test_remove_interval(self, name, intervals, to_be_removed,  expected):
        self.assertEqual(expected, RemoveInterval().remove_interval(intervals, to_be_removed))
