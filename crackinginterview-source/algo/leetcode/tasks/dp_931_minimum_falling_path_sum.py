class MinFallingPathSum:

    def min_falling_path_sum(self, a) -> int:
        if not a:
            return 0
        n = len(a)
        assert len(a[0]) == n

        for i in reversed(range(n-1)):
            for j in range(n):
                a[i][j] = a[i][j] + min(self.under_cells(a,i,j, n))

        return min(a[0][j] for j in range(n))

    def under_cells(self, f, i, j, k):
        res = [f[i + 1][j]]
        if j > 0:
            res.append(f[i+1][j - 1])
        if j < k - 1:
            res.append(f[i + 1][j + 1])
        return res
