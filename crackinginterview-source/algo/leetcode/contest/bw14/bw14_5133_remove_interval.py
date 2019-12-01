class RemoveInterval:

    def remove_interval(self, intervals, to_be_removed):
        res = []
        for interval in intervals:
            if self.not_intersect(interval, to_be_removed):
                res.append(interval)
            elif self.include_in(interval, to_be_removed):
                continue
            else:
                res.extend(self.find_not_intersected(interval, to_be_removed))
        return sorted(res, key=lambda e: e[0])

    def not_intersect(self, a, b):
        return a[1] < b[0] or b[1] < a[0]

    def include_in(self, a, b):
        return b[0] <= a[0] and a[1] <= b[1]

    def find_not_intersected(self, a, b):
        res = []
        if a[0] < b[0] and b[1] < a[1]:
            res.append([a[0], b[0]])
            res.append([b[1], a[1]])
        elif a[0] < b[0]:
            res.append([a[0], b[0]])
        elif b[1] < a[1]:
            res.append([b[1], a[1]])
        return res



