import unittest

from parameterized import parameterized

from leetcode.contest.wc165.wc165_5277_square_matrix_cnt import SquareSubMatrixCount


class TestSquareSubMatrixCnt(unittest.TestCase):

    @parameterized.expand([
        ['0',
         [
             [0, 1, 1, 1],
             [1, 1, 1, 1],
             [0, 1, 1, 1]
         ],
         15],
        ['2',
         [
             [1, 0, 1],
             [1, 1, 0],
             [1, 1, 0]
         ],
         7]
    ])
    def test_odd_cells(self, name, matrix, expected):
        self.assertEqual(expected, SquareSubMatrixCount().result(matrix))
