import unittest

from parameterized import parameterized

from leetcode.contest.wc164.wc164_5271_minimum_time_visiting_all_points import MinTimeToVisitAllPoints


class TestMinTimeToVisitAllPoints(unittest.TestCase):

    @parameterized.expand([
        ['0', [[1, 1], [3, 4], [-1, 0]], 7],
        ['1', [[3, 2], [-2, 2]], 5],
        ['2', [[100, 100]], 0],
    ])
    def test_min_time_to_visit_all_points(self, name, points, expected):
        self.assertEqual(expected, MinTimeToVisitAllPoints().min_time_to_visit_all_points(points))
