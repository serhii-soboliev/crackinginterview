import numpy as np


class NumberOfIslands:

    def num_islands(self, grid) -> int:
        m, n = np.shape(grid)
        islands_num = 0

        for i in range(m):
            for j in range(n):
                if self.is_part_of_island(grid, i, j):
                    islands_num += 1
                    self.eliminate_island(grid, i, j)
        return islands_num

    def eliminate_island(self, grid, i, j):
        grid[i][j] = '0'
        for k, l in self.get_island_neighbors(grid, i, j):
            self.eliminate_island(grid, k, l)


    def get_island_neighbors(self, grid, i, j):
        m, n = np.shape(grid)
        res = []
        if i > 0 and self.is_part_of_island(grid, i - 1, j):
            res.append((i - 1, j))
        if j > 0 and self.is_part_of_island(grid, i, j - 1):
            res.append((i, j - 1))
        if i < m-1 and self.is_part_of_island(grid, i + 1, j):
            res.append((i + 1, j))
        if j < n - 1 and self.is_part_of_island(grid, i, j+1):
            res.append((i, j + 1))
        return res

    def is_part_of_island(self, grid, i, j):
        return int(grid[i][j]) == 1