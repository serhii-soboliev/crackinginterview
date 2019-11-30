import unittest

from parameterized import parameterized

from leetcode.contest.wc162.wc162_1253_recontruct_matrix import ReconstructMatrix


class TestReconstruct2DMatrix(unittest.TestCase):

    @parameterized.expand([
        ['0', 2, 1, [1, 1, 1],
         [
             [1, 0, 1],
             [0, 1, 0]
         ]
         ],
        ['1', 2, 3, [2, 2, 1, 1], []],
        ['2', 5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1],
         [
             [1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
             [1, 1, 1, 0, 0, 0, 1, 1, 0, 0]
         ]
        ],
        ['3', 3, 0, [1, 0, 2, 2, 1], []],
        ['4', 9, 2, [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2], []]
    ])
    def test_reconstruct_2d_matrix(self, name, upper, lower, col_sum, expected):
        self.assertEqual(expected, ReconstructMatrix().reconstruct_matrix(upper, lower, col_sum))
