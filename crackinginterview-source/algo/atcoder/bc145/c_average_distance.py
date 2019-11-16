import itertools
import math


def find_path_len(p, distances):
    dist = 0
    for i in range(1, n):
        dist += distances[p[i]][p[i - 1]]
    return dist


n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

pathes = list(itertools.permutations(range(0, n)))

distances = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        s = a[i]
        f = a[j]
        d = math.sqrt((s[0] - f[0]) ** 2 + (s[1] - f[1]) ** 2)
        distances[i][j] = d
        distances[j][i] = d

pathes_length = list(map(lambda x: find_path_len(x, distances), pathes))

print(sum(pathes_length) / len(pathes_length))
