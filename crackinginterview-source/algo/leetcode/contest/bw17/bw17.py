from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def __init__(self):
        self.ssum = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node):
            if node:
                if node.val % 2 == 0:
                    if node.left:
                        if node.left.left:
                            self.ssum += node.left.left.val
                        if node.left.right:
                            self.ssum += node.left.right.val
                    if node.right:
                        if node.right.left:
                            self.ssum += node.right.left.val
                        if node.right.right:
                            self.ssum += node.right.right.val

                dfs(node.left)
                dfs(node.right)
        dfs(root)
        return self.ssum

    def distinctEchoSubstrings(self, text: str) -> int:
        results = set()
        for i in range(len(text)):
            for j in range(len(text)):
                if (j + 1 - i) % 2:
                    continue
                start = i
                end = j + 1
                middle = (start + end) // 2
                s1 = text[start:middle]
                s2 = text[middle:end]

                if s1 and s1 == s2:
                    results.add(s1)

        return len(results)

    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(0, n, 2):
            if i > n - 2:
                break
            for j in range(nums[i]):
                res.append(nums[i + 1])
        return res

    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        temp = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                s = mat[r][c]
                if r > 0:
                    s += temp[r - 1][c]
                if c > 0:
                    s += temp[r][c - 1]
                if r > 0 and c > 0:
                    s -= temp[r - 1][c - 1]
                temp[r][c] = s

        res = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                r0 = max(0, r - K)
                r1 = min(m - 1, r + K)
                c0 = max(0, c - K)
                c1 = min(n - 1, c + K)

                res[r][c] = temp[r1][c1]

                if c0 > 0:
                    res[r][c] -= temp[r1][c0 - 1]
                if r0 > 0:
                    res[r][c] -= temp[r0 - 1][c1]
                if c0 > 0 and r0 > 0:
                    res[r][c] += temp[r0 - 1][c0 - 1]
        return res

    def distinctEchoSubstrings(self, text: str) -> int:
        s = text
        if not s:
            return 0
        if len(s) == 1:
            return 0
        n = len(s)
        cnt = 0
        for center in range(0, n):
            i = center
            j = center+1

            while i >= 0 and j < n and s[i] == s[j]:
                cnt += 1
                i -= 1
                j += 1
        return cnt






