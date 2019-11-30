import unittest

from parameterized import parameterized

from leetcode.tasks.dp_198_house_robber import HouseRobber


class TestHouseRobber(unittest.TestCase):

    @parameterized.expand([
        ['0', [1, 2, 3, 1], 4],
        ['1', [2, 7, 9, 3, 1], 12]
    ])
    def test_min_cost_climbing_stairs(self, name, nums, expected):
        self.assertEqual(
            expected,
            HouseRobber().rob(nums),
            msg="Maximum spoil for test #{} is {}".format(name, expected)
        )
