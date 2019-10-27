import math


def dist(p1, p2):
    return round(math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2), 2)


def find_bitonic_tsp(p):
    p.sort(key = lambda x: x[0])
    n = len(p)
    l = [[0 for _ in range(n)] for _ in range(n)]
    N = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(1, n):
        for i in range(0, j+1):
            if i == 0 and j == 1:
                l[i][j] = dist(p[i], p[j])
                N[i][j] = j - 1
            elif j > i + 1:
                l[i][j] = l[i][j - 1] + dist(p[j - 1], p[j])
                N[i][j] = j - 1
            else:
                l[i][j] = math.inf
                for k in range(0, i):
                    q = l[k][i] + dist(p[k], p[j])
                    if q < l[i][j]:
                        l[i][j] = q
                        N[i][j] = k

    k = 0
    i = n - 2
    j = n - 1
    s = [[], []]
    while j > 0:
        s[k].append(j)
        j = N[i][j]
        if j < i:
            t = i
            i = j
            j = t
            k = 1 - k
    s[0].append(0)
    s[0].reverse()

    return s




