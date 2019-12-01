import unittest

from parameterized import parameterized

from leetcode.contest.bw14.bw14_5132_hex import Hex


class TestHex(unittest.TestCase):

    @parameterized.expand([
        ['0', "747823223228", "AEIDBCDIBC"],
        ['1', "257", "IOI"],
        ['2', "3", "ERROR"],
    ])
    def test_odd_cells(self, name, inc,  expected):
        self.assertEqual(expected, Hex().to_hex_speak(inc))
