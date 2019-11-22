import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


x, y = map(int, input().split())

if (x + y) % 3 != 0 or (2*x - y) % 3 != 0 or (x + y) // 3 < 1 or (2*x - y) // 3 < 1:
    print(0)
else:
    res = ncr((x + y) // 3, (2*x - y) // 3) % (10 ** 9 + 7)
    print(int(res))
