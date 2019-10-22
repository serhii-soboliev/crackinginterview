from scipy.sparse.csgraph import floyd_warshall
import numpy as np


def solve():
    infinity = 10 ** 10
    n, m, le = map(int, input().split())
    paths = np.full((n, n), infinity)
    for i in range(n):
        paths[i, i] = 0

    for _ in range(m):
        a, b, c = map(int, input().split())
        paths[a - 1, b - 1] = paths[b - 1, a - 1] = c

    paths = floyd_warshall(paths)
    paths = floyd_warshall(paths <= le)
    paths[np.isinf(paths)] = 0

    q = int(input())
    answer = []
    for _ in range(q):
        s, t = map(int, input().split())
        answer.append(int(paths[s - 1][t - 1] - 1))

    print("\n".join(map(str, answer)))


if __name__ == "__main__":
    solve()
