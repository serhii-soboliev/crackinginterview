class MaxAreaOfIsland:

    def max_area_of_island(self, grid) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.find_area_of_island(grid, i, j, n, m))
        return max_area

    def find_area_of_island(self, grid, i, j, n, m):
        if grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        area = 1
        for k, l in self.get_neighbours(grid, i, j, n, m):
            area += self.find_area_of_island(grid, k, l, n, m)
        return area

    def get_neighbours(self, grid, i, j, n, m):
        res = []
        if i > 0 and grid[i - 1][j] == 1:
            res.append((i - 1, j))
        if j > 0 and grid[i][j - 1] == 1:
            res.append((i, j - 1))
        if i < n - 1 and grid[i + 1][j] == 1:
            res.append((i + 1, j))
        if j < m - 1 and grid[i][j + 1] == 1:
            res.append((i, j + 1))
        return res
