from typing import List


class Solution:

    def __init__(self):
        self.max_depth = 0
        self.ssum = 0

    def deepestLeavesSum(self, root) -> int:
        def dfs(node, depth=0):
            if node:
                if depth > self.max_depth:
                    self.max_depth = depth
                    self.ssum = node.val
                elif depth == self.max_depth:
                    self.ssum += node.val

                dfs(node.left, depth + 1)
                dfs(node.right, depth + 1)

        dfs(root)

        return self.ssum

    def find_best_value(self, arr: List[int], target: int) -> int:
        arr.sort()
        min_sum = float('inf')
        left_sum = 0
        left_idx = 0
        min_idx = 0

        for t in range(max(arr) + 1):
            while left_idx < len(arr) and arr[left_idx] < t:
                left_sum += arr[left_idx]
                left_idx += 1

            converted_sum = left_sum + (len(arr) - left_idx) * t
            if abs(converted_sum - target) < abs(min_sum - target):
                min_sum = converted_sum
                min_idx = t

        return min_idx

    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n - 1):
            maxx = arr[i + 1]
            for j in range(i + 2, n):
                maxx = max(maxx, arr[j])
            arr[i] = maxx
        arr[n - 1] = -1
        return arr

    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None



