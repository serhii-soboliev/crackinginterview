class NumberOfIslands:

    def num_islands(self, grid) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        islands_num = 0

        for i in range(m):
            for j in range(n):
                if self.is_part_of_island(grid, i, j):
                    islands_num += 1
                    self.eliminate_island(grid, i, j, m, n)
        return islands_num

    def eliminate_island(self, grid, i, j, m, n):
        grid[i][j] = '0'
        for k, l in self.get_island_neighbors(grid, i, j, m, n):
            self.eliminate_island(grid, k, l, m, n)

    def get_island_neighbors(self, grid, i, j, m, n):
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
        return grid[i][j] == '1'