import numpy as np
from scipy.sparse.csgraph import floyd_warshall
import sys

input = sys.stdin.readline


def solve():
    INF = float("Inf")
    n, m, l = map(int, input().split())
    G = [[INF] * n for i in range(n)]
    for i in range(n):
        G[i][i] = 0
    for i in range(m):
        a, b, c = map(int, input().split())
        a, b = a - 1, b - 1
        if c <= l:
            G[a][b] = G[b][a] = c
    G = floyd_warshall(G, directed=False)
    G = np.where(G <= l, 1, INF)
    for i in range(n):
        G[i][i] = 0
    GG = floyd_warshall(G, directed=False)

    q = int(input())
    ans = []
    for i in range(q):
        s, t = map(int, input().split())
        a = GG[s - 1][t - 1]
        if a == INF:
            a = 0
        else:
            a = int(a)
        ans.append(a - 1)
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()