import unittest
from algo.DailyCodingProblem import ConsCarCdr


class TestConsCarCdr(unittest.TestCase):

    def test_car(self):
        ccc = ConsCarCdr()
        self.assertEqual(ccc.car(ccc.cons(3, 5)), 3)
        self.assertEqual(ccc.cdr(ccc.cons(3, 5)), 5)