class ClimbingStairs:

    def climb_stairs(self, n) -> int:
        distinct_ways = [0]*(n+1)
        distinct_ways[0] = 1
        distinct_ways[1] = 1
        for i in range(2,n+1):
            distinct_ways[i] = distinct_ways[i - 1] + distinct_ways[i - 2]
        return distinct_ways[n]



