import unittest

from parameterized import parameterized

from leetcode.contest.wc162.wc162_1252_cell_with_odd_values import CellWithOddValues


class TestCellWithOddValue(unittest.TestCase):

    @parameterized.expand([
        ['0', 2, 3, [[0, 1], [1, 1]], 6],
        ['0', 2, 2, [[1, 1], [0, 0]], 0],
    ])
    def test_odd_cells(self, name, m,n, indices, expected):
        self.assertEqual(expected, CellWithOddValues().oddCells(m, n, indices))
        self.assertEqual(expected, CellWithOddValues().oddCells2(m, n, indices))
