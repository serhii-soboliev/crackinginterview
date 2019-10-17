import unittest
from parameterized import parameterized

from graph.graph import Graph


class TestGraph(unittest.TestCase):

    @parameterized.expand([
        ['1', [1,2,3], [[1,2], [1,3], [2,3]], 'Vertices']
    ])
    def test_graph_str(self, name, e, v, expected):
        self.assertTrue(str(Graph(e, v)).startswith(expected))
