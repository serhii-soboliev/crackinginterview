def solve():
    a, b, x = map(int, input().split())
    p = len(str(x))
    maxx = 0
    for i in range(1, p + 1):
        le = x - b * i
        t = le // a
        p1 = len(str(t))
        cur_max = t if i > p1 else (10 ** i - 1)
        maxx = max(cur_max, maxx)
    print(maxx)


if __name__ == "__main__":
    solve()
