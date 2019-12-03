from functools import lru_cache


class StoneGame:

    def result1(self, piles) -> bool:
        n = len(piles)
        max_cost = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            max_cost[i][i] = piles[i]

        for size in range(2, n+1):
            for start in range(0, n-size+1):
                end = start + size - 1
                if end < n:
                    max_cost[start][end] = max(piles[start] - max_cost[start + 1][end],
                                               piles[end] - max_cost[start][end - 1])
        return max_cost[0][n - 1] > 0


    def result2(self, piles) -> bool:
        n = len(piles)
        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j:
                return 0
            parity = (j - i - n) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, n - 1) > 0

    def result3(self, piles):
        n = len(piles)

        max_cost = [[0 for _ in range(n+2)] for _ in range(n+2)]

        for size in range(1, n+1):
            for i in range(n-size+1):
                j = i + size - 1
                if (i + j + n) % 2 == 1:
                    max_cost[i+1][j+1] = max(piles[i] + max_cost[i + 2][j+1], piles[j] + max_cost[i+1][j])
                else:
                    max_cost[i+1][j+1] = min(-piles[i] + max_cost[i + 2][j+1], -piles[j] + max_cost[i+1][j])

        return max_cost[1][n] > 0
