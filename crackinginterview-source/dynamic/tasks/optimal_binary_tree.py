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

    def find_optimal(self, p, q):
        assert len(p) == len(q)
        e, root = self.find_e_root(p, q)
        return e[1][len(p)-1]

    def find_e_root(self, p, q):
        assert len(p) == len(q)
        n = len(p)
        e = [[0 for i in range(n)] for j in range(n+1)]
        w = [[0 for i in range(n)] for j in range(n+1)]
        root = [[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(n):
            q_cur = q[i]
            e[i+1][i] = q_cur
            w[i+1][i] = q_cur

        for l in range(1, n+1):
            for i in range(1, n-l+1):
                j = i + l - 1
                e[i][j] = 1000
                w_cur = w[i][j-1] + p[j] + q[j]
                w[i][j] = w_cur
                for r in range(i, j+1):
                    t = e[i][r-1] + e[r+1][j] + w[i][j]
                    if t < e[i][j]:
                        e[i][j] = t
                        root[i][j] = r
        return e, root

