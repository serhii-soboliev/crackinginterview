import unittest

from parameterized import parameterized

from atcoder.bc145.e_all_you_can_eat import all_you_can_eat


class TestAllYouCanEat(unittest.TestCase):

    @parameterized.expand([
        ['1', 2, 60, [10, 100], [10, 100], 110],
        ['2', 3, 60, [30, 30, 30], [10, 20, 30], 50],
        ['3', 10, 100, [15, 20, 13, 24, 18, 19, 23, 18, 27, 22], [23, 18, 17, 12, 29, 27, 21, 20, 15, 25], 145]
    ])
    def test_all_you_can_eat(self, name, n, t, a, b, expected):
        self.assertEqual(
            expected,
            all_you_can_eat(n, t, a, b),
            "Achievable happiness for test # {} is {}".format(name, expected)
        )