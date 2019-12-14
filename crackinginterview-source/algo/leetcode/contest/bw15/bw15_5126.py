class Solution5126:

    def find_special_integer(self, arr) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]

        p = n // 4
        cur_cnt = 1
        for i in range(1, n):
            if cur_cnt > p:
                return arr[i - 1]
            if cur_cnt > 0:
                if arr[i - 1] == arr[i]:
                    cur_cnt += 1
                else:
                    cur_cnt = 0
            else:
                cur_cnt = 1
        return arr[-1]
