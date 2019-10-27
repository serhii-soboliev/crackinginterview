def calc_max_height_team(n, t1, t2):
    mht = [[0 for i in range(n)] for j in range(3)]
    if n == 1:
        return max(t1[0], t2[0])
    mht[0][0] = t1[0]
    mht[1][0] = t2[0]
    mht[2][0] = 0
    for i in range(1, n):
        mht[0][i] = max(mht[1][i - 1] + t1[i], mht[2][i - 1] + t1[i])
        mht[1][i] = max(mht[0][i - 1] + t2[i], mht[2][i - 1] + t2[i])
        mht[2][i] = max(mht[0][i - 1], mht[1][i - 1])
    return max(mht[0][n - 1], mht[1][n - 1])


def solve():
    n = int(input())
    f_t = list(map(lambda x: int(x), input().split()))
    s_t = list(map(lambda x: int(x), input().split()))
    print(int(calc_max_height_team(n, f_t, s_t)))


solve()

