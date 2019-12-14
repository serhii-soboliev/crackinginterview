from itertools import combinations


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        n = len(characters)
        cl = combinationLength
        self.dictionary = list(filter(lambda x: len(x) == cl, [''.join(s) for i in range(n) for s in combinations(characters, i+1)]))
        self.ln = len(self.dictionary)
        self.current = 0

    def next(self) -> str:
        el = self.dictionary[self.current]
        self.current += 1
        return el

    def hasNext(self) -> bool:
        return self.current < self.ln
