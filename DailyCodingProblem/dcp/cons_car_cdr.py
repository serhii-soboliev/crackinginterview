class ConsCarCdr:

    def cons(self, a, b):
        def pair(f):
            return f(a, b)

        return pair

    def car(self, pair):
        def first(a, b):
            return a
        return pair(first)

    def cdr(self, pair):
        def second(a, b):
            return b
        return pair(second)