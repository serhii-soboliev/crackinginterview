import unittest

from parameterized import parameterized

from leetcode.tasks.dp_712_minimum_ascii_delete_sum_for_two_strings import minimum_delete_sum, \
    minimum_delete_sum_bottom_up


class TestMin(unittest.TestCase):

    @parameterized.expand([
        ['0', 'sea', 'eat',  231],
        ['0', 'delete', 'leet',  403]
    ])
    def test_minimum_delete_sum(self, name, s1, s2,  expected):
        self.assertEqual(minimum_delete_sum(s1, s2), expected)
        self.assertEqual(minimum_delete_sum_bottom_up(s1, s2), expected)


if __name__ == '__main__':
    unittest.main()