import unittest

from parameterized import parameterized

from DailyCodingProblem.dcp.array_of_products import ArrayOfProducts


class TestArrayOfProducts(unittest.TestCase):

    @parameterized.expand([
        ['1', [1, 2, 3, 4, 5], [120, 60, 40, 30, 24]],
        ['2', [3, 2, 1], [2, 3, 6]],
        ['3', [], []]
    ])
    def test_array_of_products(self, name, input, expected):
        self.assertEqual(
            ArrayOfProducts(input).build_products(),
            expected
        )