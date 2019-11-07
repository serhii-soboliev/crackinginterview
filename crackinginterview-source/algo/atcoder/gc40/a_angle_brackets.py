def calc(n):
    return n * (n + 1) // 2


def solve():
    s = list(input())
    res = find_sum(s)
    print(res)


def find_sum(S):
    prev = S[0]
    series = 1
    l = []
    for i in range(1, len(S)):
        if prev == S[i]:
            series += 1
        else:
            l.append((prev, series))
            prev = S[i]
            series = 1
    l.append((prev, series))
    prev_max = l[0][1]
    prev = calc(prev_max)
    res = prev
    for s, n in l[1::]:
        if s == '<':
            prev = calc(n)
            prev_max = n
            res += prev
        else:
            if n >= prev_max:
                res -= prev_max
                prev = calc(n)
                res += prev
            else:
                prev = calc(n - 1)
                res += prev

    return res


if __name__ == "__main__":
    solve()
