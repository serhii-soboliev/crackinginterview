class CountingBits:

    def result(self, n: int):
        res = [0 for _ in range(n + 1)]
        res[0] = 0
        pow_2 = []
        st = 1
        while st <= n:
            pow_2.append(st)
            st *= 2

        cur_last_pow_2 = 0
        for i in range(1, n+1):
            if i in pow_2:
                res[i] = 1
                cur_last_pow_2 = i
            else:
                shift = i - cur_last_pow_2
                res[i] = 1 + res[shift]
        return res
