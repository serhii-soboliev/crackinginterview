
class LongestCommonSubSequence:

    def lcs(self, s1, s2):
        if self.is_blank(s1) or self.is_blank(s2):
            return ""
        l1 = len(s1) - 1
        l2 = len(s2) - 1
        if s1[l1] == s2[l2]:
            return self.lcs(s1[:-1], s2[:-1]) + s1[l1]
        else:
            c1 = self.lcs(s1, s2[:-1])
            c2 = self.lcs(s1[:-1], s2)
            return c1 if len(c1) > len(c2) else c2

    def is_blank(self, s):
        return not (s and s.strip())