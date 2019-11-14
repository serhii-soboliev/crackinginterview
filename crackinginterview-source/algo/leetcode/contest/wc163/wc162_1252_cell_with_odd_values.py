class CellWithOddValues:

    def oddCells(self, n, m, indices) -> int:
        a = [[0 for _ in range(m)] for _ in range(n)]
        for i, j in indices:
            for k in range(m):
                a[i][k] += 1
            for k in range(n):
                a[k][j] += 1
        odd_cnt = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] % 2 == 1:
                    odd_cnt += 1
        return odd_cnt

    def oddCells2(self, n, m, indices) -> int:
        rows = [0 for _ in range(n)]
        cols = [0 for _ in range(m)]
        for i, j in indices:
            rows[i] += 1
            cols[j] += 1

        even_rows = sum(x % 2 == 0 for x in rows)
        odd_rows = n - even_rows
        even_cols = sum(x % 2 == 0 for x in cols)
        odd_cols = m - even_cols

        return odd_rows * even_cols + even_rows * odd_cols