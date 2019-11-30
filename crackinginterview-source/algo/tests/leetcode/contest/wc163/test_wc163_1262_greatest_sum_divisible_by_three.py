import unittest

from parameterized import parameterized

from leetcode.contest.wc163.wc163_1262_greates_sum_divisible_by_three import GreatestSumDivisibleByThree


class TestGreatestSumDivisibleByThree(unittest.TestCase):

    @parameterized.expand([
        ['0', [3, 6, 5, 1, 8], 18],
        ['1', [4], 0],
        ['2', [1, 2, 3, 4, 4], 12],
    ])
    def test_greatest_sum_divisible_by_three(self, name, nums, expected):
        self.assertEqual(expected, GreatestSumDivisibleByThree().max_sum_div_three(nums))
