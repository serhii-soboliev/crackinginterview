class BestTimeToBuyAndSellStock:

    def max_profit(self, prices) -> int:
        if not prices:
            return 0
        n = len(prices)
        max_profits = [0 for _ in range(n + 1)]
        min_price = [0 for _ in range(n + 1)]
        min_price[1] = prices[0]
        for i in range(1, n):
            max_profits[i + 1] = max(max_profits[i], prices[i] - min_price[i])
            min_price[i + 1] = min(min_price[i], prices[i])
        return max_profits[n]
