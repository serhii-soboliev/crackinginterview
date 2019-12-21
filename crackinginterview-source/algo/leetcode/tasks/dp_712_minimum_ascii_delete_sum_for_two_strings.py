def minimum_delete_sum(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    min_sum = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(1, n + 1):
        min_sum[i][0] = min_sum[i - 1][0] + ord(s1[i - 1])

    for i in range(1, m + 1):
        min_sum[0][i] = min_sum[0][i - 1] + ord(s2[i - 1])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                min_sum[i][j] = min_sum[i - 1][j - 1]
            else:
                min_sum[i][j] = min(min_sum[i - 1][j] + ord(s1[i - 1]), min_sum[i][j - 1] + ord(s2[j - 1]))

    return min_sum[-1][-1]


def minimum_delete_sum_bottom_up(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in reversed(range(len(s1))):
        dp[i][len(s2)] = dp[i + 1][len(s2)] + ord(s1[i])
    for j in reversed(range(len(s2))):
        dp[len(s1)][j] = dp[len(s1)][j + 1] + ord(s2[j])

    for i in reversed(range(len(s1))):
        for j in reversed(range(len(s2))):
            if s1[i] == s2[j]:
                dp[i][j] = dp[i + 1][j + 1]
            else:
                dp[i][j] = min(dp[i + 1][j] + ord(s1[i]),
                               dp[i][j + 1] + ord(s2[j]))

    return dp[0][0]
