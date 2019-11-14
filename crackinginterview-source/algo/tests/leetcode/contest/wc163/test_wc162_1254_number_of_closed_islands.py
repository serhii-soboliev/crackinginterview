import unittest

from parameterized import parameterized

from algo.leetcode.contest.wc162.wc162_1254_number_of_closed_islands import NumberOfClosedIslands


class TestMaxAreaOfIsland(unittest.TestCase):

    @parameterized.expand([
        ['0',
         [
             [1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 1, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 1, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1]
         ], 2
        ],
        ['1',
         [
             [1, 1, 1, 1, 1, 1, 1, 0],
             [1, 0, 0, 0, 0, 1, 1, 0],
             [1, 0, 1, 0, 1, 1, 1, 0],
             [1, 0, 0, 0, 0, 1, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 0]
         ], 2
        ],
        ['2',
         [
             [0, 0, 1, 0, 0],
             [0, 1, 0, 1, 0],
             [0, 1, 1, 1, 0]
         ], 1
        ],
        ['3', [], 0]
    ])
    def test_closed_islands(self, name, grid, expected):
        self.assertEqual(expected, NumberOfClosedIslands().closed_island_count(grid))
