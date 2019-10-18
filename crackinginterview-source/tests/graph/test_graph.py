import unittest
from parameterized import parameterized

from graph.graph import Graph


class TestGraph(unittest.TestCase):

    @parameterized.expand([
        ['1', [1, 2, 3], [[1, 2], [1, 3], [2, 3]], 'Vertices']
    ])
    def test_graph_str(self, name, e, v, expected):
        self.assertTrue(str(Graph(e, v)).startswith(expected))

    @parameterized.expand([
        ['1', [1, 2, 3, 4, 5, 6], [[1, 2], [1, 3], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6], [5, 6]], 2, 2, 0],
        ['2', [1, 2, 3, 4, 5, 6], [[1, 2], [1, 3], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6], [5, 6]], 1, 5, 4],
        ['3', [1, 2, 3, 4, 5, 6], [[1, 2], [1, 3], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6], [5, 6]], 1, 6, 5]
    ])
    def test_graph_find_longest_acyclic_path_recursive(self, name, v, e, v_from, v_to, expected):
        self.assertEqual(
            Graph(v, e).find_longest_acyclic_path_recursive(v_from, v_to),
            expected,
            "Error in test #" + name)

    @parameterized.expand([
        ['1', [1, 2, 3, 4, 5, 6], [[1, 2], [1, 3], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6], [5, 6]], 2, 2, 0],
        ['2', [1, 2, 3, 4, 5, 6], [[1, 2], [1, 3], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6], [5, 6]], 1, 5, 4],
        ['3', [1, 2, 3, 4, 5, 6], [[1, 2], [1, 3], [2, 3], [2, 5], [3, 4], [4, 5], [4, 6], [5, 6]], 1, 6, 5]
    ])
    def test_graph_find_longest_acyclic_path_optimal(self, name, v, e, v_from, v_to, expected):
        self.assertEqual(
            Graph(v, e).find_longest_acyclic_path_optimal(v_from, v_to),
            expected,
            "Error in test #" + name)
