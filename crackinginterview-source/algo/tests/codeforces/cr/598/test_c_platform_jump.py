import unittest

from parameterized import parameterized

from codeforces.cr.n598.с_platform_jump import jump_program


class TestPlatformJump(unittest.TestCase):

    @parameterized.expand([
        ['1', 7, 3, 2, [1, 2, 1], [0, 1, 0, 2, 2, 0, 3]],
        ['2', 10, 1, 11, [1], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    ])
    def test_platform_jump(self, name, n, m, d, c, expected):
        self.assertEqual(
            jump_program(n, m, d, c)[1],
            expected
        )

    def test_platform_jump_special_case(self):
        platforms = [4,3,4,4,6,1,4,3,4,1,4,1,4,2,2,3,2,6,3,2,6,1,1,4,1,2,4,2,3,2,5,2,3,4,3,3,3,2,5,4,2,5,4,2,2,4,4,2,4,1,3,5,4,4,5,3,6,5,3,3,4,4,2,3,3,3,1,4,4,3,2,3,2,5,4,3,2,4,3,1,2,5,6,2,3,6,3,2,2,2,2,2,6,4,4,5,5,1,4,2,5,1,6,4,2,2,3,7,2,3,3,2,4,4,2,3,2,3,3,4,1,3,2,3,2,7,7,3,3,3,4,2,2,3,2,3,4,2,3,3,4,3,3,5,2,3,1,2,6,5,4,2,6,2,3,2,3,4,3,1,2,7,5,3,6,4,1,4,4,4,5,3,2,1,2,3,4,3,2,4,2,2,3,1,2,2,5,1,1,4,1,4,3,5,3,2,3,5,3,4,4,4,4,7,2,3,1,3,3,2,3,2,5,4,1,1,4,4,5,2,3,2,3,4,2,3,1,3,2,4,1,2]
        _, res = jump_program(1000, 232, 105, platforms)
        self.assertEqual(res[965:969], [9,9,9,9])


