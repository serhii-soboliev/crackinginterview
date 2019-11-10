import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dfs_200_number_of_islands import NumberOfIslands


class TestNumberOfIslands(unittest.TestCase):

    @parameterized.expand([
        ['1',
         [
             ['1', '1', '1', '1', '0'],
             ['1', '1', '0', '1', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0']
         ], 1],
        ['2',
         [
             ['1', '1', '0', '0', '0'],
             ['1', '1', '0', '0', '0'],
             ['0', '0', '1', '0', '0'],
             ['0', '0', '0', '1', '1']
         ], 3],
        ['3',
         [
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0'],
             ['0', '0', '0', '0', '0']
         ], 0],
        ['4',
         [
             ['1', '0', '1', '0', '1'],
             ['0', '1', '0', '1', '0'],
             ['1', '0', '1', '0', '1'],
             ['0', '1', '0', '1', '0'],
             ['1', '0', '1', '0', '1']
         ], 13],
        ['5',
         [
             ['1', '1', '0', '0', '1'],
             ['1', '1', '0', '0', '1'],
             ['0', '0', '1', '1', '0'],
             ['0', '0', '1', '1', '0']
         ], 3],
        ['6', [], 0]

    ])
    def test_num_islands(self, name, grid, expected):
        self.assertEqual(NumberOfIslands().num_islands(grid), expected)


if __name__ == '__main__':
    unittest.main()
