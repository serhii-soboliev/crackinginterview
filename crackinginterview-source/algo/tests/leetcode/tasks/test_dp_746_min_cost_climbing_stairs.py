import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_746_min_cost_climbing_stairs import MinCostClimbingStairs


class TestMinCostClimbingStairs(unittest.TestCase):

    @parameterized.expand([
        ['0', [10, 15, 20], 15],
        ['1', [1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6]
    ])
    def test_min_cost_climbing_stairs(self, name, cost, expected):
        self.assertEqual(
            expected,
            MinCostClimbingStairs().min_cost_climbing_stairs(cost),
            msg="Minimal cost of climbing stairs for test # {} must be {}".format(name, expected)
        )
