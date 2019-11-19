import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_322_coin_change import CoinChange


class TestCoinChange(unittest.TestCase):

    @parameterized.expand([
        ['0', [1, 2, 5], 11, 3],
        ['1', [2], 3, -1]
    ])
    def test_coin_change(self, name, coins, amount, expected):
        self.assertEqual(
            expected,
            CoinChange().coin_change(coins, amount),
            msg="On Test#{} result must be {}".format(name, expected)
        )
