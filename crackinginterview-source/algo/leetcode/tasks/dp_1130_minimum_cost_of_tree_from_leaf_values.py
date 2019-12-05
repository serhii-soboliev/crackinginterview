class MctFromLeafValues:

    def result(self, arr) -> int:
        n = len(arr)
        non_leaf_sum = [[0 for _ in range(n)] for _ in range(n)]
        for size in range(2, n+1):
            for start in range(0, n-size+1):
                end = start + size - 1
                cur_min = float("inf")
                for k in range(start, end):
                    k_min = non_leaf_sum[start][k] + non_leaf_sum[k+1][end] + max(arr[start:k+1]) * max(arr[k+1:end+1])
                    cur_min = min(cur_min,k_min)
                non_leaf_sum[start][end] = cur_min
        return non_leaf_sum[0][n - 1]

    def result_greedy(self, arr):
        ans = 0
        while len(arr) > 1:
            n = len(arr)
            temp = float("inf")
            index = 0
            for i in range(n - 1):
                mul = arr[i] * arr[i + 1]
                if mul < temp:
                    index = i
                    temp = mul
            ans += temp
            if arr[index] < arr[index + 1]:
                arr.pop(index)
            else:
                arr.pop(index + 1)

        return ans
