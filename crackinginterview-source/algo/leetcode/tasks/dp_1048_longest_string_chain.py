from typing import List


def longest_string_chain(a: List[int]) -> int:
   return 0


def is_predecessor(a: str, b: str) -> bool:
    m = len(a)
    n = len(b)
    if m + 1 != n:
        return False
    not_equal = 0
    i = j = 0
    while i < m and j < n:
        if a[i] != b[j]:
            not_equal += 1
            j += 1
        else:
            i += 1
            j += 1

    return not_equal + (n - j) < 2



