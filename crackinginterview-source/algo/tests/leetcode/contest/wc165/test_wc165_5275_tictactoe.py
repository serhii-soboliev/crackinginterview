import unittest

from parameterized import parameterized

from leetcode.contest.wc165.wc165_5275_tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    @parameterized.expand([
        ['0', [[0,0],[2,0],[1,1],[2,1],[2,2]], "A"],
        ['1', [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], "B"],
        ['3', [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], "Draw"],
        ['4', [[0,0],[1,1]], "Pending"]
    ])
    def test_odd_cells(self, name, moves,  expected):
        self.assertEqual(expected, TicTacToe().result(moves))
