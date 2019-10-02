import unittest
from parameterized import parameterized
from codeforces.ecr73.d_make_fence_great_again.d_make_fence_great_againV1 import great_fence_cost as great_fence_costV1


class TestMakeFenceGreatAgain(unittest.TestCase):

    @parameterized.expand([
        ['1', 3, [2, 2, 3], [4, 1, 5], 2],
        ['2', 3, [2, 2, 2], [3, 10, 6], 9],
        ['3', 4, [1, 3, 2, 1000000], [7, 3, 6, 2], 0]
    ])
    def test_great_fence_cost(self, name,  n, a, b, expected):
        self.assertEqual(
            great_fence_costV1(n, a, b),
            expected
        )

