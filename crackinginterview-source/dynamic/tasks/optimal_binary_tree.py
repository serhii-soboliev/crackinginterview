class OptimalBinaryTree:

    def find_recursive(self, p, q):
        assert len(p) == len(q)
        r = self.find_recursive_in_bounds(p, q, 1, 2)
        return r

    def find_recursive_in_bounds(self, p, q, i, j):
        if j == i - 1:
            return q[i - 2]
        if j == i:
            return 0
        else:
            w = self.w(p, q, i, j)
            mini = 1000
            for r in range(i, j+1):
                left = self.find_recursive_in_bounds(p, q, i, r - 1)
                right = self.find_recursive_in_bounds(p, q, r + 1, j)
                cur_min = w + left + right
                mini = min(mini, cur_min)
            return mini

    def w(self, p, q, i, j):
        return sum(map(lambda x: p[x], range(i, j))) + sum(map(lambda x: q[x], range(i-1, j)))
