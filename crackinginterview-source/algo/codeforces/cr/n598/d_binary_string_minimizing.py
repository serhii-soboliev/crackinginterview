for _ in range(int(input())):
    n, k = map(int, input().split())
    o = ['1'] * n
    for i, v in enumerate(i for i, c in enumerate(input()) if c == '0'):
        d = min(v - i, k)
        k -= d
        o[v - d] = '0'
    print(''.join(o))


def minimize_binary(n, k, s):
    s = list(s)
    putzerohere = 0
    for i in range(n):
        if s[i] == '0':
            if i - putzerohere <= k:
                k -= (i - putzerohere)
                s[i], s[putzerohere] = s[putzerohere], s[i]
                putzerohere += 1
            else:
                s[i], s[i - k] = s[i - k], s[i]
                break
    return ''.join(s)


def solve():
    q = int(input())
    for _ in range(q):
        n, k = map(int, input().split())
        s = input()
        print(minimize_binary(n, k, s))


if __name__ == "__main__":
    solve()
