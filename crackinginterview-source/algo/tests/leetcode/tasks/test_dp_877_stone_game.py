import unittest

from leetcode.tasks.dp_877_stone_game import StoneGame
from parameterized import parameterized


class TestStoneGame(unittest.TestCase):

    @parameterized.expand([
        ['0', [5, 3, 4, 5], True]
    ])
    def test_num_islands(self, name, piles, expected):
        self.assertEqual(StoneGame().result1(piles), expected)
        self.assertEqual(StoneGame().result2(piles), expected)
        self.assertEqual(StoneGame().result3(piles), expected)


if __name__ == '__main__':
    unittest.main()
