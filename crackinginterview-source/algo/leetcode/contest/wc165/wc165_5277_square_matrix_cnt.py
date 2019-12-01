class SquareSubMatrixCount:

    def result(self, matrix):
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])

        matrix_cnt = 0
        for i in range(n):
            for j in range(m):
                matrix_cnt += self.matrix_count(matrix, i, j, n, m)
        return matrix_cnt

    def matrix_count(self, matrix, k, t, n, m):
        max_len = min(n - k, m - t)
        mc = 0
        for i in range(1, max_len+1):
            sm = self.getsubgrid(matrix, k, t, k + i, t + i)
            if self.is_square(sm, i):
                mc += 1
            else:
                break
        return mc

    def is_square(self, matrix, le):
        return sum(sum(matrix, [])) == le ** 2

    def getsubgrid(self, grid, x1, y1, x2, y2):
        sublist = []
        for x in range(x1, x2):
            sublist.append(grid[x][y1:y2])
        return sublist
