import unittest

from parameterized import parameterized

from leetcode.tasks.bfs_695_max_area_of_island import MaxAreaOfIsland


class TestMaxAreaOfIsland(unittest.TestCase):

    @parameterized.expand([
        ['0',
         [
             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
             [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
         ], 6
        ],
        ['1',
         [
             [0, 0, 0, 0, 0, 0, 0, 0]
         ], 0
        ],
        ['2',
         [
             [0, 0, 0, 0, 0, 1, 1, 0]
         ], 2
        ],
        ['3',
         [
             [0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1]
         ], 1
        ],
        ['4', [], 0],
        ['5',
             [
                 [1, 1, 0, 0, 0],
                 [1, 1, 0, 0, 0],
                 [0, 0, 0, 1, 1],
                 [0, 0, 0, 1, 1]
             ], 4
         ]

    ])
    def test_surrounded_regions(self, name, grid, expected):
        self.assertEqual(expected, MaxAreaOfIsland().max_area_of_island(grid))


if __name__ == '__main__':
    unittest.main()
