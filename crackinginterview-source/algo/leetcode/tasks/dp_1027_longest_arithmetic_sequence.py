from collections import defaultdict
from typing import List


def longest_arithmetic_sequence_length(A: List[int]) -> int:
    dp = defaultdict(lambda: 1)
    dp[(A[1] - A[0], 1)] = 2
    for i in range(2, len(A)):
        for j in range(i):
            interval = A[i] - A[j]
            dp[(interval, i)] = 2 if (interval, j) not in dp else dp[(interval, j)] + 1
    return max(dp.values())
