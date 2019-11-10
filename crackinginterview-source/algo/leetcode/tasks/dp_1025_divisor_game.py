

class DivisorGame:

    def divisor_game(self, n: int) -> bool:
        return self.can_you_win(num=n, is_your_move=True)

    def can_you_win_math(self, n: int) -> bool:
        if n % 2 == 0:
            return True
        else:
            return False

    def can_you_win_opt(self, n):
        return self.build_memo_table(n, self.build_divisors(n))[True][n]

    def can_you_win(self, num, is_your_move):
        if is_your_move:
            if num == 2:
                return True
            if num == 1:
                return False
            else:
                return any(map(lambda x: self.can_you_win(num - x, False), self.get_number_divisors(num)))
        else:
            if num == 1:
                return True
            if num == 2:
                return False
            else:
                return all(map(lambda x: self.can_you_win(num - x, True), self.get_number_divisors(num)))

    def build_memo_table(self, n: int, divisors:dict) -> dict:
        res = {True: {}, False: {}}
        res[True][1] = False
        res[True][2] = True
        res[False][1] = True
        res[False][2] = False

        for i in range(3, n+1):
            res[True][i] = any(map(lambda x: res[False][i - x], divisors[i]))
            res[False][i] = all(map(lambda x: res[True][i - x], divisors[i]))
        return res

    def get_number_divisors(self, num):
        for i in range(1, int(num / 2) + 1):
            if num % i == 0:
                yield i

    def build_divisors(self, num):
        res = {}
        for n in range(num+1):
            res[n] = list(self.get_number_divisors(n))
        return res
