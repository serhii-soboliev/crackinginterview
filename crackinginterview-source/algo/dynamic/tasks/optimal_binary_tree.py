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
        root = [[0 for i in range(n-1)] for j in range(n-1)]
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
                        root[i-1][j-1] = r
        return e, root

    def build_tree_trace_from_root(self, roots):
        left = 0
        right = len(roots[0]) - 1
        root_element = roots[left][right]
        tree_trace = ["k%s is the root" % root_element]
        self.build_obt_from_roots_between_indexes(roots, left, root_element-2, root_element, "left", tree_trace)
        self.build_obt_from_roots_between_indexes(roots, root_element, right, root_element, "right", tree_trace)
        return tree_trace

    def build_obt_from_roots_between_indexes(self, roots, left, right, p_root, child_side, tree_trace):
        n = len(roots[0])
        if left < 0 or right < 0 or left > n-1 or right > n-1:
            d_num = p_root if child_side == "right" else p_root - 1
            tree_trace.append("d%s is %s child of k%s" % (d_num, child_side, p_root))
            return
        cur_root = roots[left][right]
        if cur_root == p_root or cur_root == 0:
            d_num = p_root if child_side == "right" else p_root - 1
            tree_trace.append("d%s is %s child of k%s" % (d_num, child_side, p_root))
            return
        tree_trace.append("k%s is %s child of k%s" % (cur_root, child_side, p_root))
        self.build_obt_from_roots_between_indexes(roots, left, cur_root - 2, cur_root, "left", tree_trace)
        self.build_obt_from_roots_between_indexes(roots, cur_root, right, cur_root, "right", tree_trace)