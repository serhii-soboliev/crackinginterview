import unittest

from parameterized import parameterized

from leetcode.tasks.dp_70_climbing_stairs import ClimbingStairs


class TestClimbingStairs(unittest.TestCase):

    @parameterized.expand([
        ['0', 2, 2],
        ['1', 3, 3]
    ])
    def test_min_cost_climbing_stairs(self, name, n, expected):
        self.assertEqual(
            expected,
            ClimbingStairs().climb_stairs(n),
            msg="Ways to climb {} stairs is {}".format(n, expected)
        )
