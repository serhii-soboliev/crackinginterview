# https://codeforces.com/problemset/problem/1221/D


def helper(h1, h2, h3, a, b, c, h):
    mini = 2 * (10 ** 18)
    if h1 != h:
        mini = min(mini, a)
    if h2 != h:
        mini = min(mini, b)
    if h3 != h:
        mini = min(mini, c)
    return mini


def solve():
    query_number = int(input())
    for k in range(query_number):
        n = int(input())
        h = [0]*n
        p = [0]*n
        for j in range(n):
            h[j], p[j] = list(map(int, input().split(" ")))

        a = 0
        b = p[0]
        c = p[0] * 2

        for i in range(1,n):
            a_new = helper(h[i - 1], h[i - 1] + 1, h[i - 1] + 2, a, b, c, h[i]) + 0
            b_new = helper(h[i - 1], h[i - 1] + 1, h[i - 1] + 2, a, b, c, h[i] + 1) + p[i] * 1
            c_new = helper(h[i - 1], h[i - 1] + 1, h[i - 1] + 2, a, b, c, h[i] + 2) + p[i] * 2
            a = a_new
            b = b_new
            c = c_new
        print(min(a,b,c))

solve()
