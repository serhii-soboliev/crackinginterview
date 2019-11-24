import unittest

from parameterized import parameterized

from algo.leetcode.contest.wc164.wc164_5274_number_of_ways_to_stay_at_same_place import NumberOfWaysToStayAtSamePlace


class TestNumberOfWaysToStayAtSamePlace(unittest.TestCase):

    @parameterized.expand([
        ['0', 3, 2, 4],
        ['1', 2, 4, 2],
        ['2', 4, 2, 8],
    ])
    @unittest.skip("Not implemented yet")
    def test_min_time_to_visit_all_points(self, name, steps, arrLen, expected):
        self.assertEqual(expected,
                         NumberOfWaysToStayAtSamePlace().numWays(steps, arrLen),
                         "Number of ways to stay at same place for Test # {} must be {}".format(name, expected))
