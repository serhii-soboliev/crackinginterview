class MinimumCostForTickets:

    def min_cost_tickets(self, days, costs):
        if not days:
            return 0
        n = days[-1] + 1
        dp = [0] * n
        for day in days:
            dp[day] = float('inf')
        for i in range(1, n):
            if dp[i] == float('inf'):
                dp[i] = min(dp[i - 1] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i - 30, 0)] + costs[2])
            else:
                dp[i] = dp[i - 1]
        return dp[-1]
