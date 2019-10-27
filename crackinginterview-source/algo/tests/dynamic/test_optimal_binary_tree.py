import unittest
from parameterized import parameterized

from algo.dynamic.tasks.optimal_binary_tree import OptimalBinaryTree


class TestOptimalBinaryTree(unittest.TestCase):

    def setUp(self):
        self.obt = OptimalBinaryTree()

    @parameterized.expand([
        ['1', [0, 0.15, 0.1, 0.05, 0.1, 0.2], [0.05, 0.1, 0.05, 0.05, 0.05, 0.1], 2.75]
    ])
    def test_find_recursive(self, name, p, q, expected_cost):
        recursive = self.obt.find_recursive(p, q)
        self.assertEqual(recursive, expected_cost)

    @parameterized.expand([
        ['1', [0, 0.15, 0.1, 0.05, 0.1, 0.2], [0.05, 0.1, 0.05, 0.05, 0.05, 0.1], 2.75],
        ['2', [0, 0.04, 0.06, 0.08, 0.02, 0.1, 0.12, 0.14], [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05], 3.12]
    ])
    def test_find_optimal(self, name, p, q, expected_cost):
        recursive = self.obt.find_optimal(p, q)
        self.assertEqual(recursive, expected_cost)

    @parameterized.expand([
       ['1', [0, 0.15, 0.1, 0.05, 0.1, 0.2], [0.05, 0.1, 0.05, 0.05, 0.05, 0.1],
            ['k2', 'k1', 'd0', 'd1', 'k5', 'k4', 'k3', 'd2', 'd3', 'd4', 'd5']],
       ['2', [0, 0.04, 0.06, 0.08, 0.02, 0.1, 0.12, 0.14], [0.06, 0.06, 0.06, 0.06, 0.05, 0.05, 0.05, 0.05],
            ['k5', 'k2', 'k1', 'd0', 'd1', 'k3', 'd2', 'k4', 'd3', 'd4', 'k7', 'k6', 'd5', 'd6', 'd7']]
    ])
    def test_build_obt_from_root(self, name, p, q, expected_obt_tree):
        e, root = self.obt.find_e_root(p, q)
        tree_trace = self.obt.build_tree_trace_from_root(root)
        self.assertEquals(expected_obt_tree, list(map(lambda s: s[:2], tree_trace)))


