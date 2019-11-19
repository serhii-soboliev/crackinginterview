class CoinChange:

    def coin_change(self, coins, amount: int) -> int:
        n = amount + 1
        dp = [amount+1] * n
        dp[0] = 0
        coins.sort()
        for i in range(1,n):
            for coin in coins:
                if coin <= amount:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                else:
                    break

        return dp[amount] if dp[amount] <= amount else -1

