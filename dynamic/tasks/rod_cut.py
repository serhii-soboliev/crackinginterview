import logging as log

class RodCut:

    def __init__(self, prices):
        self.prices = prices
        self.memoized_result = {0:0}
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
        log.basicConfig(format=FORMAT, level=log.DEBUG)

    def find_optimum_cut_top_down_recursive(self, length=10):
        log.debug(f'Looking for optimum cut for length =  {length}')
        if length == 0:
            return 0
        q = 1
        for i in range(1,length+1):
            q = max(q, self.prices[i] + self.find_optimum_cut_top_down_recursive(length - i))
        log.debug(f'Optimum cut for length {length} is {q}')
        return q

    def find_optimum_cut_top_down_memoization(self, length=10):
        self.fill_rod_cut_memoized_result(length)
        return self.memoized_result[length]

    def find_optimum_cut_bottom_up(self, length=10):
        r = {0:0}
        for j in range(1, length+1):
            q = 1
            for i in range(1, j+1):
                q = max(q, self.prices[i] + r[j - i])
            r[j] = q
        return r[length]

    def fill_rod_cut_memoized_result(self, length=10):
        for i in range(0, length+1):
            self.memoized_result[i] = self.calculate_memoized_rod_cut(i)

    def calculate_memoized_rod_cut(self, length=10):
        if length == 0:
            return 0
        q = 1
        for i in range(1,length + 1):
            q = max(q, self.prices[i] + self.memoized_result[length - i])
        return q

    def find_optimum_cut_bottom_up_with_first_piece(self, length=10):
        r = {0:0}
        s = {0:0}
        for j in range(1, length+1):
            q = -1
            for i in range(1, j+1):
                if q < self.prices[i] + r[j-i]:
                    q = self.prices[i] + r[j-i]
                    s[j] = i
            r[j] = q
        return r,s

    def find_rod_cut_value_and_solution(self, length=10):
        r,s = self.find_optimum_cut_bottom_up_with_first_piece(length)
        solution = []
        current_length = length
        while current_length > 0:
            solution.append(s[current_length])
            current_length -= s[current_length]
        return r[length],solution





