import unittest

from parameterized import parameterized

from leetcode.contest.bw15.bw15_5126 import Solution5126
from leetcode.contest.bw15.bw15_5127_remove_covered_intervals import Solution5127
from leetcode.contest.bw15.bw15_5129_falling_path_ll import Solution5129


class TestBW15(unittest.TestCase):

    @parameterized.expand([
        ['0', [1,2,3,3], 3],
        ['1', [1], 1],
        ['2', [1,2,2,6,6,6,6,7,10], 6]
    ])
    def test_find_special_integer(self, name, arr,  expected):
        self.assertEqual(expected, Solution5126().find_special_integer(arr))

    @parameterized.expand([
        ['0', [[1,4],[3,6],[2,8]], 2]
    ])
    def test_find_special_integer(self, name, arr,  expected):
        self.assertEqual(expected, Solution5127().remove_covered_intervals(arr))

    @parameterized.expand([
        ['0', [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 13],
        ['1', [
               [-73, 61, 43, -48, -36],
               [3, 30, 27, 57, 10],
               [96, -76, 84, 59, -15],
               [5, -49, 76, 31, -7],
               [97, 91, 61, -46, 67]], -192],
        ['2', [
               [-37, 51, -36, 34, -22],
               [82, 4, 30, 14, 38],
               [-68, -52, -92, 65, -85],
               [-49, -3, -77, 8, -19],
               [-60, -71, -21, -62, -73]], -268]

    ])
    def test_min_falling_path_sum(self, name, a, expected):
        self.assertEqual(Solution5129().min_falling_path_sum(a), expected)
