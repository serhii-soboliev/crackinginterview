from dynamic.tasks.longest_common_subsequence import LongestCommonSubSequence


class String:

    _in_str = ""

    def __init__(self, in_str):
        self._in_str = in_str

    def find_longest_palindrome_subsequence(self):
        return LongestCommonSubSequence().lcs(str(self), self.reverse())

    def __str__(self) -> str:
        return self._in_str

    def reverse(self) -> str:
        return ''.join(reversed(self._in_str))

