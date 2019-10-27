import sys

input = sys.stdin.readline
import math


def solve():
    a, b, x = (int(i) for i in input().split())
    L = a * a * b
    if L <= x:
        print(0)
    else:
        mi = 0
        ma = 89.999999999
        while ma - mi >= 10 ** (-9):
            next = (mi + ma) / 2
            bairitu = math.tan(math.radians(next))
            if x >= L / 2:
                lim = L - (a ** 3 / 2) * round(bairitu, 10)
            else:
                lim = (0.5) * a * b * b * math.tan(math.radians(90 - next))
            if x > lim:
                ma = next
            else:
                mi = next
        print(ma)


solve()
