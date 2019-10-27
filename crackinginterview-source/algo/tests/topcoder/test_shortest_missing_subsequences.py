import unittest

from parameterized import parameterized

from algo.topcoder.shortest_missing_subsequences import ShortestMissingSubsequences


class TestShortestMissingSubsequences(unittest.TestCase):

    def setUp(self):
        self.sms = ShortestMissingSubsequences()

    @parameterized.expand([
        ['1', 3, 4,  [1, 0, 0, 1],                   [[0, 0, 0], [0, 1, 0], [0, 1, 1], [1, 1, 0], [1, 1, 1]]],
        ['2', 5, 4,  [1, 0, 0, 1],                   [[2], [3], [4]]],
        ['3', 3, 10, [1, 2, 0, 0, 1, 2, 1, 2, 2, 2], [[0, 0, 0], [0, 1, 0], [0, 2, 0], [1, 1, 0], [2, 1, 0],  [2, 2, 0]]]
    ])
    @unittest.skip("Not implemented yet")
    def test_build(self, name, g, n, a, expected):
        self.assertCountEqual(
            self.sms.build(g, n, a),
            expected
        )

    @parameterized.expand([
        ['1', 3, 4, [1, 0, 0, 1], [3, 5]],
        ['2', 5, 4, [1, 0, 0, 1], [1, 3]],
        ['3', 3, 10, [1, 2, 0, 0, 1, 2, 1, 2, 2, 2], [3, 6]],
        ['4', 7, 7,  [0, 1, 2, 3, 4, 5, 6], [2, 28]],
        ['5', 7, 14, [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6], [2, 21]]
    ])
    @unittest.skip("Not implemented yet")
    def test_count(self, name, g, n, a, expected):
        self.assertCountEqual(
            self.sms.count(g, n, a),
            expected
        )
