import unittest

from DailyCodingProblem.dcp.xor_linked_list import XorLinkedList


class TestXorLinkedList(unittest.TestCase):

    def test_xor_linked_list_add(self):
        xll = XorLinkedList()
        xll.add(100)
        xll.add(200)
        xll.add(300)
        self.assertEqual(xll.get(0).val, 100)
        self.assertEqual(xll.get(1).val, 200)
        self.assertEqual(xll.get(2).val, 300)
        self.assertEqual(xll.size(), 3)
        xll.add(400)
        self.assertEqual(xll.get(2).val, 300)
        self.assertEqual(xll.get(3).val, 400)
        self.assertEqual(xll.size(), 4)
