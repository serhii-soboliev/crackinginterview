class OptimalBinaryTree:

    def find_recursive(self, p, q):
        assert len(p) == len(q)
        r = self.find_recursive_in_bounds(p, q, 1, len(p)-1)
        return r

    def find_recursive_in_bounds(self, p, q, i, j):
        if j == i - 1:
            return q[i - 1]

        min_obt_cost = 1000
        for r in range(i, j + 1):
            w = self.w(p, q, i, j)
            left = self.find_recursive_in_bounds(p, q, i, r - 1)
            right = self.find_recursive_in_bounds(p, q, r + 1, j)
            min_obt_cost = min(w + left + right, min_obt_cost)
        return min_obt_cost

    def w(self, p, q, i, j):
        sum1 = sum(map(lambda x: p[x], range(i, j + 1)))
        sum2 = sum(map(lambda x: q[x], range(i - 1, j + 1)))
        return sum1 + sum2
