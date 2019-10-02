import unittest
from parameterized import parameterized

from dynamic.tasks.optimal_binary_tree import OptimalBinaryTree


class TestOptimalBinaryTree(unittest.TestCase):

    def setUp(self):
        self.obt = OptimalBinaryTree()


    @parameterized.expand([
        ['1', [0, 0.15, 0.1, 0.05, 0.1, 0.2], [0.05, 0.1, 0.05, 0.05, 0.05, 0.1], 2.75]
    ])
    def test_find_recursive(self, name, p, q, expected_cost):
        recursive = self.obt.find_recursive(p, q)
        #TODO Fix obt search
        #self.assertEqual(recursive, expected_cost)
