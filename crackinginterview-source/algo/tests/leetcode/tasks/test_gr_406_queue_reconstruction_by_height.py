import unittest

from parameterized import parameterized

from algo.leetcode.tasks.gr_406_queue_reconstruction_by_height import Solution


class TestQueueReconstruction(unittest.TestCase):

    @parameterized.expand([
        ['0', [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]], [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]],
    ])
    def test_queue_reconstruction_by_height(self, name, people, expected):
        self.assertEqual(
            expected,
            Solution().reconstructQueue(people)
        )
