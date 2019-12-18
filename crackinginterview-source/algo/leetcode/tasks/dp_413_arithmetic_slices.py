from typing import List


def number_of_arithmetic_slices(A: List[int]) -> int:
    if not A:
        return 0
    a = A
    n = len(a)
    dp = [0 for _ in range(n)]

    for i in range(2, n):
        a_s_cnt = 0
        diff = a[i] - a[i - 1]
        diff_hold = True
        nxt = i - 2
        while nxt >= 0 and diff_hold:
            if a[nxt+1] - a[nxt] == diff:
                a_s_cnt += 1
                nxt -= 1
            else:
                diff_hold = False

        dp[i] = dp[i - 1] + a_s_cnt

    return dp[n - 1]