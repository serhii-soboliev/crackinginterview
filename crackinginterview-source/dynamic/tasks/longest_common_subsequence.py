from os import stat_result

import numpy as np

class LongestCommonSubSequence:

    def lcs_recursive(self, s1, s2):
        if self.is_blank(s1) or self.is_blank(s2):
            return ""
        l1 = len(s1) - 1
        l2 = len(s2) - 1
        if s1[l1] == s2[l2]:
            return self.lcs_recursive(s1[:-1], s2[:-1]) + s1[l1]
        else:
            c1 = self.lcs_recursive(s1, s2[:-1])
            c2 = self.lcs_recursive(s1[:-1], s2)
            return c1 if len(c1) > len(c2) else c2

    def lcs(self, s1, s2):
        m = len(s1)
        n = len(s2)
        lcs = [["" for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + s1[i-1]
                else:
                    lcs[i][j] = lcs[i-1][j] if len(lcs[i-1][j]) > len(lcs[i][j-1]) else lcs[i][j-1]
        return lcs[m][n]

    def is_blank(self, s):
        return not (s and s.strip())
