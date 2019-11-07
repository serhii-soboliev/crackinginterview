import unittest

from parameterized import parameterized

from algo.leetcode.dp_1025_divisor_game import DivisorGame


class TestDivisorGame(unittest.TestCase):

    @parameterized.expand([
        ['1', 1, False],
        ['2', 2, True],
        ['3', 3, False],
        ['4', 4, True],
        ['5', 5, False],
        ['5', 6, True],
    ])
    def test_can_you_win(self, name, num, expected):
        self.assertEqual(expected, DivisorGame().can_you_win(num, True))

    @parameterized.expand([
         ['1', 1, False],
         ['2', 2, True],
         ['3', 3, False],
         ['4', 4, True],
         ['5', 5, False],
         ['6', 6, True],
    ])
    def test_can_you_win_opt(self, name, num, expected):
        self.assertEqual(expected, DivisorGame().can_you_win_opt(num))

    @parameterized.expand([
        ['1', 1, False],
        ['2', 2, True],
        ['3', 3, False],
        ['4', 4, True],
        ['5', 5, False],
        ['5', 6, True]
    ])
    def test_can_you_win_math(self, name, num, expected):
        self.assertEqual(expected, DivisorGame().can_you_win_math(num))

    @parameterized.expand([
        ['1', 1, []],
        ['2', 2, [1]],
        ['3', 3, [1]],
        ['4', 4, [1, 2]],
        ['5', 5, [1]],
        ['6', 6, [1, 2, 3]],
        ['7', 7, [1]],
        ['8', 8, [1, 2, 4]]
    ])
    def test_get_number_divisor(self, name, num, expected):
        self.assertEqual(expected, list(DivisorGame().get_number_divisors(num)))


if __name__ == '__main__':
    unittest.main()
