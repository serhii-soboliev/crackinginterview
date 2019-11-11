class SurroundedRegions:

    O = 'O'
    X = 'X'
    V = 'V'

    def solve(self, board) -> None:
        if not board:
            return
        n = len(board)
        m = len(board[0])

        sides_os = self.find_sides_os(board, n, m)

        for i, j in sides_os:
            self.mark_alligned_to_sides(board, i, j, n, m)

        self.replace_one_symbol_with_another(board, self.O, self.X, n, m)
        self.replace_one_symbol_with_another(board, self.V, self.O, n, m)

    def find_sides_os(self, board, n, m):
        board_os = []
        for i in range(n):
            if board[i][0] == self.O:
                board_os.append((i, 0))
            if board[i][m-1] == self.O:
                board_os.append((i, m-1))
        for j in range(m):
            if board[0][j] == self.O:
                board_os.append((0,j))
            if board[n-1][j] == self.O:
                board_os.append((n-1,j))
        return board_os

    def mark_alligned_to_sides(self, board, i, j, n, m):
        if board[i][j] == self.O:
            board[i][j] = self.V
            for k, l in self.get_neighbours(board, i, j, n, m):
                self.mark_alligned_to_sides(board, k, l, n, m)


    def replace_one_symbol_with_another(self, board, s1, s2, n, m):
        for i in range(n):
            for j in range(m):
                if board[i][j] == s1:
                    board[i][j] = s2

    def get_neighbours(self, board, i, j, n, m):
        res = []
        if i > 0 and board[i - 1][j] == self.O:
            res.append((i - 1, j))
        if j > 0 and board[i][j - 1] == self.O:
            res.append((i, j - 1))
        if i < n - 1 and board[i + 1][j] == self.O:
            res.append((i + 1, j))
        if j < m - 1 and board[i][j + 1] == self.O:
            res.append((i, j + 1))
        return res


class SurroundedRegions2:
    def solve(self, board) -> None:
        if not board:
            return
        n = len(board)
        m = len(board[0])
        not_surrounded_regions = set([])
        for i in range(n):
            for j in range(m):
                if (i, j) in not_surrounded_regions or board[i][j] == 'X':
                    continue
                region = []
                if self.search_for_region(board, i, j, n, m, region, not_surrounded_regions):
                    self.eliminate_region(board, region)

    def search_for_region(self, board, i, j, n, m, region, not_surrounded_regions):
        if board[i][j] == 'X' or (i, j) in region:
            return True
        if (i, j) in not_surrounded_regions:
            return False
        if board[i][j] == 'O' and self.is_border_cell(board, i, j, n, m):
            not_surrounded_regions.add((i, j))
            return False
        region.append((i, j))
        b = self.search_for_region(board, i - 1, j, n, m, region, not_surrounded_regions) \
               and self.search_for_region(board, i, j - 1, n, m, region, not_surrounded_regions) \
               and self.search_for_region(board, i + 1, j, n, m, region, not_surrounded_regions) \
               and self.search_for_region(board, i, j + 1, n, m, region, not_surrounded_regions)
        if not b:
            not_surrounded_regions |= set(region)
        return b

    def is_border_cell(self, board, i, j, n, m):
        return i == 0 or j == 0 or i == n - 1 or j == m - 1

    def eliminate_region(self, board, region):
        for i, j in region:
            board[i][j] = 'X'

