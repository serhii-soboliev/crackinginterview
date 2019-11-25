class MinCostClimbingStairs:

    def min_cost_climbing_stairs(self, cost) -> int:
        f1 = cost[0]
        f2 = cost[1]
        for x in cost[2:]:
            new = x + min(f1, f2)
            f1 = f2
            f2 = new
        return min(f1, f2)
