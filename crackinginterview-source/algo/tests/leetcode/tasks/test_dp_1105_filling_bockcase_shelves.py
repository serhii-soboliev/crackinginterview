import unittest

from parameterized import parameterized

from leetcode.tasks.dp_1105_filling_bookcase_shelves import MinHeightShelves


class TestMinHeightShelves(unittest.TestCase):

    @parameterized.expand([
        ['0', [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4, 6]
    ])
    def test_min_height_shelves(self, name, books, shelf_width, expected):
        self.assertEqual(MinHeightShelves().min_height_shelves(books, shelf_width), expected)


if __name__ == '__main__':
    unittest.main()
