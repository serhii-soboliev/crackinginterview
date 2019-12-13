import unittest

from parameterized import parameterized

from leetcode.tasks.dp_1140_stone_game_2 import StoneGame2


class TestStoneGame2(unittest.TestCase):

    @parameterized.expand([
       # ['0', [2, 7, 9, 4, 4], 10],
        ['1', [1, 5, 7, 9, 9], 17],
    ])
    def test_num_islands(self, name, piles, expected):
        # self.assertEqual(StoneGame2().stone_game_II(piles), expected)
        self.assertEqual(StoneGame2().stone_game_ll_v2(piles), expected)


if __name__ == '__main__':
    unittest.main()
