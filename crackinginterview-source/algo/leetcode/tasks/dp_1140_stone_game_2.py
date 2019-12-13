from functools import lru_cache
from typing import List


class StoneGame2:

    def stone_game_ll(self, piles: List[int]) -> int:

        @lru_cache(None)
        def dfs(p, m, f):
            if p > len(piles):
                return 0

            if f == 'L':
                # Lee tries to minimize the piles Alex can get
                return min([dfs(p + i, max(m, i), 'A') for i in range(1, 2 * m + 1)])
            else:
                # Alex tries to maximize the piles Alex can get
                return max(sum(piles[p:][:i]) + dfs(p + i, max(m, i), 'L') for i in range(1, 2 * m + 1))

        return dfs(0, 1, 'A')

    def stone_game_ll_v2(self, piles: List[int]) -> int:
        n = len(piles)

        def dp(p, m, t):
            if (p, m, t) not in memo:

                if p > n:
                    memo[p, m, t] = 0
                elif t == "L":
                    memo[p, m, t] = min(dp(p + i, max(i, m), "A") for i in range(1, 2 * m + 1))
                else:
                    memo[p, m, t] = max(sum(piles[p:][:i]) + dp(p + i, max(i, m), "L") for i in range(1, 2 * m + 1))

            return memo[p, m, t]

        memo = {}
        return dp(0, 1, 'A')
