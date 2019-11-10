def solve():
    n = int(input())
    d = list(map(int, input().split()))

    print(calc(d, n))


def calc(d, n):
    if d[0] != 0:
        return 0
    else:
        k = max(d)
        a = [0] * (k + 1)
        for i in range(1, n):
            a[d[i]] += 1
        if a[0] > 0:
            return 0
        else:
            r = 1
            for i in range(2, k + 1):
                r *= a[i - 1] ** a[i]
            return r % 998244353


if __name__ == "__main__":
    solve()
