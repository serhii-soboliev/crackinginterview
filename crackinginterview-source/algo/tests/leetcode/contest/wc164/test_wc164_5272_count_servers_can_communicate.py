import unittest

from parameterized import parameterized

from algo.leetcode.contest.wc164.wc164_5272_count_servers_can_communicate import CountServerCanCommunicate


class TestCountServersCanCommunicate(unittest.TestCase):

    @parameterized.expand([
        ['0', [[1, 0], [0, 1]], 0],
        ['1', [[1, 0], [1, 1]], 3],
        ['2', [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]], 4],
    ])
    def test_min_time_to_visit_all_points(self, name, grid, expected):
        self.assertEqual(expected, CountServerCanCommunicate().count_server_can_communicate(grid))
