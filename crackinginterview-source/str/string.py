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

    def __str__(self) -> str:
        return self._in_str

    def reverse(self) -> str:
        return ''.join(reversed(self._in_str))
