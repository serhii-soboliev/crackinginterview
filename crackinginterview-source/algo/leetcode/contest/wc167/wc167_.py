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
        paths = [(0, 0, 0, 0)]
        visited = {(0, 0, 0)}
        possible_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def target_reached(x_, y_):
            return x_ == n - 1 and y_ == m - 1

        def possible_to_be_there(x_, y_):
            return 0 <= x_ < n and 0 <= y_ < m

        while paths:
            x, y, z, path_len = paths.pop(0)
            if target_reached(x, y):
                return path_len
            for p_d in possible_directions:
                new_x, new_y = x + p_d[0], y + p_d[1]
                if possible_to_be_there(new_x, new_y):
                    if grid[new_x][new_y] == 1:
                        if z < k and (new_x, new_y, z + 1) not in visited:
                            visited.add((new_x, new_y, z + 1))
                            paths.append((new_x, new_y, z + 1, path_len + 1))
                    else:
                        if (new_x, new_y, z) not in visited:
                            visited.add((new_x, new_y, z))
                            paths.append((new_x, new_y, z, path_len + 1))
        return -1

class ListNode:
    def __init__(self, x, l):
        self.val = x
        self.next = l
