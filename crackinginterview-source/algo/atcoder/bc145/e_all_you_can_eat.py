def all_you_can_eat(n, t, a, b):
    dp = [[0 for _ in range(2)] for _ in range(t)]
    for x in range(n):
        for i in reversed(range(t)):
            if i + a[x] < t:
                dp[i + a[x]][0] = max(dp[i + a[x]][0], dp[i][0] + b[x])
                dp[i + a[x]][1] = max(dp[i + a[x]][1], dp[i][1] + b[x])
            dp[i][1] = max(dp[i][1], dp[i][0] + b[x])
    return dp[t-1][1]


def solve():
    n, t = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a[i], b[i] = map(int, input().split())

    print(all_you_can_eat(n, t, a, b))


if __name__ == "__main__":
    solve()
