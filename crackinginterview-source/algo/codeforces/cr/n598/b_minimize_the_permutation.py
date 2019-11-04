def minimize_permutation(n, p):
    ops = [False] * (n-1)
    lp = 0
    for k in range(1, n+1):
        i = p.index(k)
        if i == lp:
            lp += 1
        else:
            for j in reversed(range(lp, i)):
                if ops[j]:
                    break
                t = p[j]
                p[j] = p[j + 1]
                p[j + 1] = t
                ops[j] = True
        lp = k

    return ' '.join(map(str, p))


def solve():
    q = int(input())
    for _ in range(q):
        n = int(input())
        p = list(map(int, input().split()))
        print(minimize_permutation(n, p))


if __name__ == "__main__":
    solve()
