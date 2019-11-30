import unittest

from parameterized import parameterized

from leetcode.tasks.dp_983_minimum_cost_for_tickets import MinimumCostForTickets


class TestMinimumCostForTickets(unittest.TestCase):

    @parameterized.expand([
        ['0', [1, 4, 6, 7, 8, 20], [2, 7, 15], 11],
        ['1', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17],
        ['2', [], [2, 7, 15], 0],
        ['2', [65], [2, 7, 15], 2]
    ])
    def test_minimum_cost_of_tickets(self, name, days, cost, expected):
        self.assertEqual(
            expected,
            MinimumCostForTickets().min_cost_tickets(days, cost),
            msg="Test Minimum Cost of Tickets # {} result must be {}".format(name, expected)
        )
