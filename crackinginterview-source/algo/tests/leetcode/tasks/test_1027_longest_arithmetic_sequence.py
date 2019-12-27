import unittest

from parameterized import parameterized

from algo.leetcode.tasks.dp_1027_longest_arithmetic_sequence import longest_arithmetic_sequence_length

class TestLongestArithmeticSequence(unittest.TestCase):

    @parameterized.expand([
        ['0', [83, 20, 17, 43, 52, 78, 68, 45], 2],
        ['1', [9, 4, 7, 2, 10], 3],
        ['2', [20, 1, 15, 3, 10, 5, 8], 4]
    ])
    def test_longest_arithmetic_sequence(self, name, A,  expected):
        self.assertEqual(expected, longest_arithmetic_sequence_length(A))
