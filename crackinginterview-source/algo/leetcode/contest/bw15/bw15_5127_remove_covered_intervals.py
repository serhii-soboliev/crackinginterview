class Solution5127:

    def remove_covered_intervals(self, intervals) -> int:
        not_covered = 0
        n = len(intervals)
        intervals2 = intervals.copy()
        for i in range(n):
            interval = intervals[i]
            covered = False
            for j in range(n):
                if i == j:
                    continue
                cur_interval = intervals2[j]
                if self.is_covered(interval, cur_interval):
                    covered = True
                    break
            if not covered:
                not_covered += 1

        return not_covered

    def is_covered(self, i1, i2):
        return i2[0]  <= i1[0] and i1[1] <= i2[1]