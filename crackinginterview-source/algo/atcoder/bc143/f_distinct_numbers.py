from collections import Counter
import bisect


def solve():
    num = int(input())
    al = list(map(int, input().split()))
    c = list(Counter(al).values())
    c.sort()
    ln = len(c)

    d = [ln - bisect.bisect_left(c, x) for x in range(num + 1)]
    s = [0]
    for n in range(1, num + 1):
        s.append(s[-1] + d[n])

    t = [x / s[x] for x in range(1, num + 1)]

    solution = []

    for k in range(1, num + 1):
        solution.append(bisect.bisect_right(t, 1 / k))

    print("\n".join(map(str, solution)))


if __name__ == "__main__":
    solve()
