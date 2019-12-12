from dynamic.tasks.longest_common_subsequence import LongestCommonSubSequence
from utils.constants import EMPTY


class String:
    _in_str = EMPTY

    def __init__(self, in_str):
        self._in_str = in_str

    def find_longest_palindrome_subsequence_using_reverse(self):
        return LongestCommonSubSequence().lcs(str(self), self.reverse())

    def find_longest_palindrome_subsequence_length(self):
        p = self.build_longest_palindrome_subsequence_dict()
        return p[0][len(self._in_str) - 1]

    def build_longest_palindrome_subsequence_dict(self):
        n = len(self._in_str)
        p = [[EMPTY for _ in range(n)] for _ in range(n)]
        for i in range(n):
            p[i][i] = self._in_str[i]

        for sublen in range(2, n+1):
            for i in range(n-sublen+1):
                j = i + sublen - 1
                if self._in_str[i] == self._in_str[j]:
                    if sublen == 2:
                        p[i][j] = self._in_str[i] + self._in_str[j]
                    else:
                        p[i][j] = self._in_str[i] + p[i+1][j-1] + self._in_str[j]
                else:
                    p[i][j] = max(p[i+1][j], p[i][j-1], key=len)
        return p

    def is_subsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        n = len(s)
        cur_s_index = 0
        cur_letter = s[0]
        for letter in t:
            if cur_letter == letter:
                cur_s_index += 1
                if cur_s_index == n:
                    return True
                cur_letter = s[cur_s_index]
        return False

    def palindrome_partitioning_3(self, s: str, k: int) -> int:
        n = len(s)
        dp = [[0 for _ in range(k+1)] for _ in range(n)]
        for i in range(n):
            max_partition = min(i + 1, k)
            prefix = s[:i + 1]
            dp[i][1] = self.cost_to_make_palindrome_from_string(prefix)
            for j in range(2, max_partition+1):
                curr_min = n
                for p in range(j - 1, i+1):
                    suffix = prefix[p:]
                    curr_min = min(curr_min, dp[p - 1][j - 1] + self.cost_to_make_palindrome_from_string(suffix))
                dp[i][j] = curr_min
        return dp[n-1][k]

    def palindrome_partitioning_3_v2(self, s: str, k: int) -> int:
        n = len(s)

        def dp(i, p):
            if (i,p) not in memo:
                if p == 1:
                    memo[i,p] = self.cost_to_make_palindrome_from_string(s[:i+1])
                else:
                    memo[i, p] = min(
                        dp(j, p-1) + self.cost_to_make_palindrome_from_string(s[j + 1:i + 1]) for j in range(p - 2, i)
                    )
            return memo[i,p]

        memo = {}
        return dp(n-1, k)


    def cost_to_make_palindrome_from_string(self, s: str) -> int:
        n = len(s)
        cost = 0
        for i in range(n // 2):
            cost += (s[i] != s[n - i - 1])
        return cost

    def __str__(self) -> str:
        return self._in_str

    def reverse(self) -> str:
        return ''.join(reversed(self._in_str))

