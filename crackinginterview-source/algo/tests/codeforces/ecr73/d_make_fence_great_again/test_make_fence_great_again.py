import unittest
from parameterized import parameterized
from algo.codeforces.ecr73.d_make_fence_great_again.d_make_fence_great_againV3 import great_fence_cost as great_fence_cost_v3
from algo.codeforces.ecr73.d_make_fence_great_again.d_make_fence_great_againV2 import great_fence_cost as great_fence_cost_v2
from algo.codeforces.ecr73.d_make_fence_great_again.d_make_fence_great_againV1 import great_fence_cost as great_fence_cost_v1


class TestMakeFenceGreatAgain(unittest.TestCase):

    @parameterized.expand([
        ['1', 3, [2, 2, 3], [4, 1, 5], 2],
        ['2', 3, [2, 2, 2], [3, 10, 6], 9],
        ['3', 4, [1, 3, 2, 1000000], [7, 3, 6, 2], 0],
        ['4', 3, [1, 1, 2], [9, 5, 13], 9]
    ])
    def test_great_fence_cost_v1(self, name,  n, a, b, expected):
        self.assertEqual(
            great_fence_cost_v1(n, a, b),
            expected
        )

    @parameterized.expand([
        ['1', 3, [2, 2, 3], [4, 1, 5], 2],
        ['2', 3, [2, 2, 2], [3, 10, 6], 9],
        ['3', 4, [1, 3, 2, 1000000], [7, 3, 6, 2], 0],
        ['4', 3, [1, 1, 2], [9, 5, 13], 9]
    ])
    def test_great_fence_cost_v2(self, name, n, a, b, expected):
        self.assertEqual(
            great_fence_cost_v2(n, a, b),
            expected
        )

    @parameterized.expand([
        ['1', 3, [2, 2, 3], [4, 1, 5], 2],
        ['2', 3, [2, 2, 2], [3, 10, 6], 9],
        ['3', 4, [1, 3, 2, 1000000], [7, 3, 6, 2], 0],
        ['4', 3, [1, 1, 2], [9, 5, 13], 9]
    ])
    def test_great_fence_cost_v3(self, name, n, a, b, expected):
        self.assertEqual(
            great_fence_cost_v3(n, a, b),
            expected
        )