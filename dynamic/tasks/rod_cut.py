import logging as log

class RodCut:

    def __init__(self, prices):
        self.prices = prices
        FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
        log.basicConfig(format=FORMAT, level=log.DEBUG)

    def find_optimum_cut(self, length=10):
        log.debug(f'Looking for optimum cut for length =  {length}')
        if length == 0:
            return 0
        q = -1000
        for i in range(1,length+1):
            q = max(q, self.prices[i] + self.find_optimum_cut(length-i))
        log.debug(f'Optimum cut for length {length} is {q}')
        return q
