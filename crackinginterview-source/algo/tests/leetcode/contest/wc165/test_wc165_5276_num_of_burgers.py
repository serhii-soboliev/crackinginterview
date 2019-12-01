import unittest

from parameterized import parameterized

from leetcode.contest.wc165.wc165_5276_num_of_burgers import NumOfBurgers


class TestNumOfBurgers(unittest.TestCase):

    @parameterized.expand([
        ['0', 16, 7, [1, 6]],
        ['1', 17, 4, []],
        ['2', 4, 17, []],
        ['3', 0, 0, [0, 0]],
        ['4', 2, 1, [0, 1]],
        ['4', 4, 1, [1, 0]]

    ])
    def test_odd_cells(self, name, tomato_pieces, cheese_pieces, expected):
        self.assertEqual(expected, NumOfBurgers().result(tomato_pieces, cheese_pieces))
