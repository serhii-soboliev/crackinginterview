import unittest

from parameterized import parameterized

from atcoder.bc143.d_triangles import find_triangle_count


class TestDTriangles(unittest.TestCase):

    @parameterized.expand([
        ['1', [3, 4, 2, 1], 1],
        ['2', [1, 1000, 1], 0],
        ['3', [218, 786, 704, 233, 645, 728, 389], 23],
        ['4', [10, 21, 22, 100, 101, 200, 300], 6]
    ])
    def test_find_triangle_count(self, name, input_list, expected):
        self.assertEqual(
            expected,
            find_triangle_count(input_list),
            "Wrong number of triangles for test#" + name)