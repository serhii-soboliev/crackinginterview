import unittest

from algo.DailyCodingProblem import MemoryMock


class TestMemoryMock(unittest.TestCase):

    def test_get_pointer(self):
        mm = MemoryMock()
        self.assertEqual(mm.get_pointer(1), 0)
        self.assertEqual(mm.get_pointer(2), 1)
        self.assertEqual(mm.get_pointer(3), 2)
        self.assertEqual(mm.get_pointer(1), 0)
        self.assertEqual(mm.get_pointer(2), 1)

    def test_dereference_pointer(self):
        mm = MemoryMock()
        mm.get_pointer(11)
        mm.get_pointer(22)
        mm.get_pointer(33)
        self.assertEqual(mm.dereference_pointer(0), 11)
        self.assertEqual(mm.dereference_pointer(1), 22)
        self.assertEqual(mm.dereference_pointer(2), 33)
