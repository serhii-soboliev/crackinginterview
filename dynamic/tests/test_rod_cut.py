import unittest

from parameterized import parameterized

from dynamic.tasks.rod_cut import RodCut


class TestRodCut(unittest.TestCase):

    @parameterized.expand([
        ['1', 1, 1],
        ['2', 2, 5],
        ['3', 3, 8],
        ['4', 4, 10],
        ['5', 5, 13],
        ['6', 6, 17],
        ['7', 7, 18],
        ['8', 8, 22],
        ['9', 9, 25],
        ['10', 10, 30]

    ])
    def test_rod_cut_optimum_1(self, name, length, price):
        prices = {
            1:1,
            2:5,
            3:8,
            4:9,
            5:10,
            6:17,
            7:17,
            8:20,
            9:24,
            10:30

        }
        rc = RodCut(prices)
        self.assertEqual(rc.find_optimum_cut(length), price)
