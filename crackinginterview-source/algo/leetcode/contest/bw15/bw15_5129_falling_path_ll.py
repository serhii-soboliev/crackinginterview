class Solution5129:

    def min_falling_path_sum(self, arr) -> int:
        row, col = len(arr), len(arr[0])
        dp = arr[0][:]
        n = len(arr)
        for i in range(1, n):
            last = dp[:]
            pre = [float('inf')]
            post = [float('inf')]
            for j in range(col):
                pre.append(min(pre[-1], last[j]))
            for j in range(col - 1, -1, -1):
                post.append(min(post[-1], last[j]))
            post = post[::-1]
            dp = [float('inf')] * n
            for j in range(len(arr[i])):
                dp[j] = min(pre[j], post[j + 1]) + arr[i][j]
        return min(dp)