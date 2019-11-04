def is_able_without_change(a, b, n, s):
    a_ = s // n
    b_ = s % n
    if a_ <= a:
        res = "YES" if b_ <= b else "NO"
    else:
        a_lack = a_ - a
        res = "YES" if a_lack * n + b_ <= b else "NO"
    return res


def solve():
    q = int(input())
    for _ in range(q):
        a,b,n,s = map(int, input().split())
        print(is_able_without_change(a,b,n,s))


if __name__ == "__main__":
    solve()
