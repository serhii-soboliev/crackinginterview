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

    def coin_change_bfs(self, coins, amount):
        if amount == 0:
            return 0
        value1 = [0]
        value2 = []
        nc = 0
        visited = [False] * (amount + 1)
        visited[0] = True
        while value1:
            nc += 1
            for v in value1:
                for coin in coins:
                    newval = v + coin
                    if newval == amount:
                        return nc
                    elif newval > amount:
                        continue
                    elif not visited[newval]:
                        visited[newval] = True
                        value2.append(newval)
            value1, value2 = value2, []
        return -1

