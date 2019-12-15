class Solution:
    def getDecimalValue(self, head) -> int:
        ans = 0
        while head:
            ans <<= 1
            ans += head.val
            head = head.next
        return ans

    def sequentialDigits(self, low: int, high: int):
        low_cnt = len(str(low))
        high_cnt = len(str(high))
        res = []
        for i in range(low_cnt, high_cnt + 1):
            for j in range(1, 10):
                cur = ""
                for k in range(i):
                    if k + j > 9:
                        break
                    cur += str(k + j)
                if low <= int(cur) <= high and len(cur) == i:
                    res.append(int(cur))
        return res

    def maxSideLength(self, mat, threshold: int) -> int:
        m = mat
        if not m or min([min(r) for r in m]) > threshold:
            return 0
        n1 = len(m)
        n2 = len(m[0])

        def getsubgrid(grid, x1, y1, x2, y2):
            sublist = []
            for x in range(x1, x2):
                sublist.append(grid[x][y1:y2])
            return sublist

        max_possible_side = min(n1, n2)
        for side in range(2, max_possible_side + 1):
            found = False
            for i in range(n1 - side + 1):
                if found:
                    break
                for j in range(n2 - side + 1):
                    sub_matrix = getsubgrid(m, i, j, i + side, j + side)
                    s = sum([sum(r) for r in sub_matrix])
                    if s <= threshold:
                        found = True
                        break
            if not found:
                return side - 1
        return max_possible_side

    def shortestPath(self, grid, k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        q = [(0, 0, 0, 0)]
        h = set([(0, 0, 0)])
        t = 0
        ff = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while t < len(q):
            x, y, z, d = q[t]
            if x == n - 1 and y == m - 1:
                return d
            t += 1
            for f in ff:
                xx, yy = x + f[0], y + f[1]
                if 0 <= xx < n and 0 <= yy < m:
                    if grid[xx][yy] == 1:
                        if z < k and (xx, yy, z + 1) not in h:
                            h.add((xx, yy, z + 1))
                            q.append((xx, yy, z + 1, d + 1))
                    else:
                        if (xx, yy, z) not in h:
                            h.add((xx, yy, z))
                            q.append((xx, yy, z, d + 1))
        return -1

    def shortestPath_1(self, grid, k: int) -> int:
        m = grid
        if not m:
            return -1
        n1 = len(m)
        n2 = len(m[0])
        if n1 == 1 and n2 == 1:
            return 0

        current_pathes = [[0, 0, k, 0]]
        min_obstacles = k + 1
        visited = [[min_obstacles for _ in range(n2)] for _ in range(n1)]

        min_path = n1 * n2 + 1


        def get_possible_moves(i, j, t, ln):
            res = []

            if i > 0 and (m[i - 1][j] == 0 or t > 0):
                res.append([i - 1, j, t - m[i - 1][j], ln+1])

            if (i < n1 - 1) and (m[i + 1][j] == 0 or t > 0):
                res.append([i + 1, j, t - m[i + 1][j], ln+1])

            if j > 0 and (m[i][j - 1] == 0 or t > 0):
                res.append([i, j - 1, t - m[i][j - 1], ln+1])

            if (j < n2 - 1) and (m[i][j + 1] == 0 or t > 0):
                res.append([i, j + 1, t - m[i][j + 1], ln+1])

            return res

        while current_pathes:
            p = current_pathes.pop()
            moves = get_possible_moves(p[0], p[1], p[2], p[3])
            for move in moves:
                if [move[0], move[1]] == [n1 - 1, n2 - 1]:
                    if move[3] < min_path:
                        min_path = move[3]
                elif visited[move[0]][move[1]] > k - move[2]:
                    current_pathes.append(move)
                    visited[move[0]][move[1]] = k - move[2]
        return -1 if min_path == n1 * n2 + 1 else min_path






class ListNode:
    def __init__(self, x, l):
        self.val = x
        self.next = l
