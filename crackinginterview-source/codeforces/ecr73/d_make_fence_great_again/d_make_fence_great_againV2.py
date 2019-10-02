# https://codeforces.com/problemset/problem/1221/D


def great_fence_cost(n, a, b):
    dp = [[-1] * n for i in range(3)]
    dp[0][0] = 0 * b[0]
    dp[1][0] = 1 * b[0]
    dp[2][0] = 2 * b[0]

    for i in range(1, n):
        for j in range(0, 3):
            dp[j][i] = -1
            cur_board = a[i] + j
            for k in range(0, 3):
                if (a[i - 1] + k != cur_board) and (dp[j][i] == -1 or dp[j][i] > j * b[i] + dp[k][i - 1]):
                    dp[j][i] = j * b[i] + dp[k][i - 1]

    return min(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1])


def solve():
    query_number = int(input())
    for i in range(query_number):
        n = int(input())
        a = []
        b = []
        for j in range(n):
            aj, bj = list(map(int, input().split(" ")))
            a.append(aj)
            b.append(bj)
        print(great_fence_cost(n, a, b))


if __name__ == '__main__':
    solve()

