import itertools


class NumberOfClosedIslands:

    def closed_island_count(self, grid) -> int:
        if not grid:
            return 0
        self.flood_fill_open_islands(grid)
        return self.get_islands_count(grid)

    def flood_fill_open_islands(self, grid):
        for i, j in self.get_border_islands_cells(grid):
            self.fill_open_island(grid, i, j)

    def get_islands_count(self, grid):
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if self.is_island_cell(i, j, grid):
                    count += 1
                    self.fill_open_island(grid, i, j)
        return count

    def get_border_islands_cells(self, grid):
        n = len(grid)
        m = len(grid[0])
        return list(itertools.filterfalse(
            lambda x: grid[x[0]][x[1]] == 1,
            itertools.chain(itertools.product([0], range(0, m))
                            , itertools.product([n - 1], range(0, m))
                            , itertools.product(range(0, n), [0])
                            , itertools.product(range(0, n), [m - 1]))
        ))

    def fill_open_island(self, grid, i, j):
        if grid[i][j] == 1:
            return
        grid[i][j] = 1
        for i, j in self.get_neighbor_island_cell(grid, i, j):
            self.fill_open_island(grid, i, j)

    def get_neighbor_island_cell(self, grid, i, j):
        return itertools.filterfalse(lambda x: self.is_not_island_cell(x, grid),
                                     [[i - 1, j], [i, j - 1], [i + 1, j], [i, j + 1]])

    def is_not_island_cell(self, x, grid):
        n = len(grid)
        m = len(grid[0])
        return x[0] < 0 or x[0] > n - 1 or x[1] < 1 or x[1] > m - 1 or grid[x[0]][x[1]] == 1

    def is_island_cell(self, k, l, grid):
        return not self.is_not_island_cell([k, l], grid)
