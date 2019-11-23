import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_121_best_time_to_buy_and_sell_stock import BestTimeToBuyAndSellStock


class TestBestTimeToBuyAndSellStock(unittest.TestCase):

    @parameterized.expand([
        ['0', [7, 1, 5, 3, 6, 4], 5],
        ['1', [7, 6, 4, 3, 1], 0],
        ['2', [1, 2, 3, 4, 5, 6], 5],
        ['3', [1, 10, 4, 3, 1], 9]
    ])
    def test_best_time_to_buy_and_sell_stock(self, name, prices, expected):
        self.assertEqual(
            expected,
            BestTimeToBuyAndSellStock().max_profit(prices),
            msg="Best time to buy and sell stock for test # {} must be {}".format(name, expected)
        )
