class LongestCommonSubsequence:

    def longest_common_subsequence_rec(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        if text1[-1] == text2[-1]:
            return 1 + self.longest_common_subsequence_rec(text1[:-1], text2[:-1])
        else:
            return max(
                self.longest_common_subsequence_rec(text1[:-1], text2),
                self.longest_common_subsequence_rec(text1, text2[:-1])
            )


    def longest_common_subsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        n1 = len(text1)
        n2 = len(text2)
        dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]