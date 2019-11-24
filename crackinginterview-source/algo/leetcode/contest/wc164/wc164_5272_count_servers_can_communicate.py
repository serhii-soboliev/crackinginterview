class CountServerCanCommunicate:

    def count_server_can_communicate(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        total_servers = 0
        for el in grid:
            total_servers += sum(el)
        rows = {}
        cols = {}
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] = rows.get(i, 0) + 1
                    cols[j] = cols.get(j, 0) + 1

        isolated_servers = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and rows[i] == 1 and cols[j] == 1:
                    isolated_servers += 1
        return total_servers - isolated_servers
