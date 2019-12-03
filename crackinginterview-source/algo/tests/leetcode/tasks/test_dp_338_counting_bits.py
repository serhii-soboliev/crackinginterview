import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_338_counting_bits import CountingBits


class TestNumberOfIslands(unittest.TestCase):

    @parameterized.expand([
        ['0', 2, [0, 1, 1]],
        ['1', 0, [0]],
        ['2', 5, [0, 1, 1, 2, 1, 2]]
    ])
    def test_num_islands(self, name, num, expected):
        self.assertEqual(CountingBits().result(num), expected)


if __name__ == '__main__':
    unittest.main()
