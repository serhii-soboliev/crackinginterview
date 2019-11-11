import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dfs_130_surrounded_regions import SurroundedRegions
from algo.leetcode.tasks.dfs_130_surrounded_regions import SurroundedRegions1
from algo.leetcode.tasks.dfs_130_surrounded_regions import SurroundedRegions2


class TestSurroundedRegions(unittest.TestCase):

    @parameterized.expand([
        ['0',
         [
            ["X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X"],
            ["X", "O", "X", "O", "X", "O"],
            ["O", "X", "O", "X", "O", "X"]
         ],
         [
            ["X", "O", "X", "O", "X", "O"],
            ["O", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "O"],
            ["O", "X", "O", "X", "O", "X"]
         ]
        ],
        ['1',
         [
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'O', 'X', 'X', 'X']
         ],
         [
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X', 'X'],
             ['X', 'O', 'X', 'X', 'X']
         ]
        ],
        ['2',
         [
             ['X', 'X', 'X', 'X'],
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']
         ],
         [
             ['X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X'],
             ['X', 'X', 'X', 'X'],
             ['X', 'O', 'X', 'X']
         ]
         ],
        ['3', [], []],
        ['4',
         [
             ['X', 'X'],
             ['X', 'X']
         ],
         [
             ['X', 'X'],
             ['X', 'X']
         ]
        ],
        ['5',
         [
             ["O", "O", "O", "O", "X", "X"],
             ["O", "O", "O", "O", "O", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "O", "O"]
         ],
         [
             ["O", "O", "O", "O", "X", "X"],
             ["O", "O", "O", "O", "O", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "O"],
             ["O", "X", "O", "O", "O", "O"]
         ]
        ]

    ])
    def test_surrounded_regions(self, name, grid, expected):
        SurroundedRegions().solve(grid)
        SurroundedRegions1().solve(grid)
        SurroundedRegions2().solve(grid)
        self.assertEqual(grid, expected)


if __name__ == '__main__':
    unittest.main()
