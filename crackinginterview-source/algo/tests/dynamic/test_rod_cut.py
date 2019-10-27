import unittest

from parameterized import parameterized

from algo.dynamic.tasks.rod_cut import RodCut


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
    def test_rod_cut_optimum_down_recursive(self, name, length, price):
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
        self.assertEqual(rc.find_optimum_cut_top_down_recursive(length), price)

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
    def test_rod_cut_optimum_down_memoization(self, name, length, price):
        prices = {
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 10,
            6: 17,
            7: 17,
            8: 20,
            9: 24,
            10: 30

        }
        rc = RodCut(prices)
        self.assertEqual(rc.find_optimum_cut_bottom_up(length), price)

    @parameterized.expand([
        ['1', 1, 1,  [1]],
        ['2', 2, 5,  [2]],
        ['3', 3, 8,  [3]],
        ['4', 4, 10, [2,2]],
        ['5', 5, 13, [2,3]],
        ['6', 6, 17, [6]],
        ['7', 7, 18, [1,6]],
        ['8', 8, 22, [2,6]],
        ['9', 9, 25, [3,6]],
        ['10', 10, 30, [10]]

    ])
    def test_find_rod_cut_value_and_solution(self, name, length, price, solution):
        prices = {
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 10,
            6: 17,
            7: 17,
            8: 20,
            9: 24,
            10: 30

        }
        rc = RodCut(prices)
        r, s = rc.find_rod_cut_value_and_solution(length)
        self.assertEqual(r, price)
        self.assertEqual(s, solution)

    def test_find_optimum_cut_bottom_up_with_first_piece(self):
        prices = {
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 10,
            6: 17,
            7: 17,
            8: 20,
            9: 24,
            10: 30

        }
        rc = RodCut(prices)
        r,s = rc.find_optimum_cut_bottom_up_with_first_piece(10)
        expected_r = {
            0: 0,
            1: 1,
            2: 5,
            3: 8,
            4: 10,
            5: 13,
            6: 17,
            7: 18,
            8: 22,
            9: 25,
            10: 30
        }
        self.assertEqual(r, expected_r)
        expected_s = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 2,
            5: 2,
            6: 6,
            7: 1,
            8: 2,
            9: 3,
            10: 10
        }
        self.assertEqual(s, expected_s)

    def test_find_optimum_cut_bottom_up_with_first_piece_and_cust_cost1(self):
        prices = {
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 10,
            6: 17,
            7: 17,
            8: 20,
            9: 24,
            10: 30

        }
        rc = RodCut(prices)
        r, s = rc.find_optimum_cut_bottom_up_with_first_piece_and_cust_cost(10, cost=1)
        expected_r = {
            0: 0,
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 12,
            6: 17,
            7: 17,
            8: 21,
            9: 24,
            10: 30
        }
        self.assertEqual(r, expected_r)
        expected_s = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 2,
            6: 6,
            7: 7,
            8: 2,
            9: 9,
            10: 10
        }
        self.assertEqual(s, expected_s)

    def test_find_optimum_cut_bottom_up_with_first_piece_and_cust_cost2(self):
        prices = {
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 10,
            6: 17,
            7: 17,
            8: 20,
            9: 24,
            10: 30

        }
        rc = RodCut(prices)
        r, s = rc.find_optimum_cut_bottom_up_with_first_piece_and_cust_cost(length=10, cost=2)
        expected_r = {
            0: 0,
            1: 1,
            2: 5,
            3: 8,
            4: 9,
            5: 11,
            6: 17,
            7: 17,
            8: 20,
            9: 24,
            10: 30
        }
        self.assertEqual(r, expected_r)
        expected_s = {
            0: 0,
            1: 1,
            2: 2,
            3: 3,
            4: 4,
            5: 2,
            6: 6,
            7: 7,
            8: 8,
            9: 9,
            10: 10
        }
        self.assertEqual(s, expected_s)