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
            return max(self.lcs_recursive(s1, s2[:-1]), self.lcs_recursive(s1[:-1], s2), key=len)

    def lcs(self, s1, s2):
        m = len(s1)
        n = len(s2)
        lcs = [["" for i in range(n+1)] for j in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    lcs[i][j] = lcs[i-1][j-1] + s1[i-1]
                else:
                    lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1], key=len)
        return lcs[m][n]

    def lcs_dict(self, s1, s2):
        s1_substrings = self.get_substrings(s1)
        s2_substrings = self.get_substrings(s2)
        lcs = {("",""):""}
        for sub1 in s1_substrings:
            lcs[(sub1, "")] = ""
        for sub2 in s2_substrings:
            lcs[("", sub2)] = ""
        for sub1 in s1_substrings:
            for sub2 in s2_substrings:
                if self.last_symbols_the_same(sub1, sub2):
                    lcs[(sub1, sub2)] = lcs[(sub1[:-1], sub2[:-1])] + sub1[-1:]
                else:
                    lcs[(sub1, sub2)] = max(lcs[(sub1[:-1], sub2)], lcs[(sub1, sub2[:-1])], key=len)
        return lcs[(s1, s2)]

    def last_symbols_the_same(self, s1, s2):
        return s1[-1:] == s2[-1:]

    def get_substrings(self, s):
        r = []
        for i in range(1, len(s)+1):
            r.append(s[:i])
        return r

    def is_blank(self, s):
        return not (s and s.strip())
