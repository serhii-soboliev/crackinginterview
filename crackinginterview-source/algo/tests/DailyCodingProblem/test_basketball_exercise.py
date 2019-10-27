import unittest

from parameterized import parameterized

from algo.dynamic.tasks.basketball_exercise import BasketballExercise


class TestBasketballExercise(unittest.TestCase):

    @parameterized.expand([
        ['1', 5, [9, 3, 5, 7, 3], [5, 8, 1, 4, 5], 29],
        ['2', 3, [1, 2, 9], [10, 1, 1], 19],
        ['3', 1, [7], [4], 7],
        ['4', 5, [7, 3, 3, 1, 8], [7, 2, 1, 1, 2], 21],
        ['5', 5, [1, 7, 6, 9, 1], [6, 1, 1, 7, 10], 33]
    ])
    def test_array_of_products(self, name, n, t1, t2, expected):
        self.assertEqual(
            BasketballExercise().calc_max_height_team(n, t1, t2),
            expected
        )
