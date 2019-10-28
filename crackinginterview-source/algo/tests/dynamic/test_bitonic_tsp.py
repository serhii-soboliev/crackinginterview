import unittest

from parameterized import parameterized

from algo.dynamic.tasks.bitonic_tsp import find_bitonic_tsp


class TestTravelingSalesmanProblem(unittest.TestCase):

    @parameterized.expand([
        ['1', [[0, 6], [1, 0], [2, 3], [5, 4], [6, 1], [7, 5], [8, 2]], [0, 1, 4, 6, 5, 3, 2]],
        ['2', [[0, 2], [1, 0], [2, 4], [4, 1], [5, 5]], [0, 2, 4, 3, 1]]

    ])
    def test_find_bitonic_tsp(self, name, p, expected_path):
        self.assertEqual(find_bitonic_tsp(p), expected_path)
