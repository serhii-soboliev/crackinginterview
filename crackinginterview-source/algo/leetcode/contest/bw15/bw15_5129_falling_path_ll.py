class Solution5129:

    def min_falling_path_sum(self, arr) -> int:
        n = len(arr)
        if n == 1:
            return arr[0][0]
        dp = [[0 for _ in range(n)] for _ in range(n)]

        def min2(nums):
            if nums[0] < nums[1]:
                min_idx_1, min_idx_2 = 0, 1
                min_1, min_2 = nums[0], nums[1]
            else:
                min_idx_1, min_idx_2 = 1, 0
                min_1, min_2 = nums[1], nums[0]
            for i in range(2, len(nums)):
                if nums[i] < min_1:
                    min_idx_2 = min_idx_1
                    min_idx_1 = i
                    min_2 = min_1
                    min_1 = nums[i]
                elif nums[i] < min_2:
                    min_idx_2 = i
                    min_2 = nums[i]
            return min_idx_1, min_idx_2

        for i in range(n):
            dp[0][i] = arr[0][i]
        min_idx_1, min_idx_2 = min2(dp[0])
        for i in range(1, n):
            for j in range(n):
                if j == min_idx_1:
                    dp[i][j] = dp[i - 1][min_idx_2] + arr[i][j]
                else:
                    dp[i][j] = dp[i - 1][min_idx_1] + arr[i][j]
            min_idx_1, min_idx_2 = min2(dp[i])
        return min(dp[n - 1])
