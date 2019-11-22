import numpy as np


def all_you_can_eat(n, t, a, b):
    a = np.array(a, np.int)
    b = np.array(b, np.int)

    idx = np.argsort(a)
    a = a[idx]
    b = b[idx]

    dp = np.zeros((n, t), np.int)

    for i in range(n - 1):
        dp[i + 1, :a[i]] = dp[i, :a[i]]
        dp[i + 1, a[i]:] = np.maximum(dp[i, a[i]:], dp[i, :-a[i]] + b[i])

    return np.max(dp[:, -1] + b)


def solve():
    n, t = map(int, input().split())
    a = []
    b = []
    for _ in range(n):
        a_temp, b_temp = map(int, input().split())
        a.append(a_temp)
        b.append(b_temp)

    print(all_you_can_eat(n,t,a,b))


if __name__ == "__main__":
    solve()
