import unittest

from parameterized import parameterized

from leetcode.contest.bw16.bw16 import Solution


class TestWC168(unittest.TestCase):

    @parameterized.expand([
        ['0', [4, 9, 3], 10, 3],
        ['1', [2, 3, 5], 10, 5],
        ['2', [60864, 25176, 27249, 21296, 20204], 56803, 11361],
        ['2', [20693,79539,84645,66727,81334,185,14263,53984,71844,71546], 39947, 4418]
    ])
    def test_find_best_value(self, name, arr, target, expected):
        self.assertEqual(expected, Solution().find_best_value(arr, target))
