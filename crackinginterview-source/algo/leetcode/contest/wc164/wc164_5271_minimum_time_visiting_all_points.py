class MinTimeToVisitAllPoints:

    def min_time_to_visit_all_points(self, points) -> int:
        n = len(points)
        if n == 1:
            return 0
        s = 0
        for i in range(1, n):
            cur_point = points[i]
            prev_point = points[i - 1]
            s += self.find_moves_between_points(cur_point, prev_point)
        return s

    def find_moves_between_points(self, p1, p2):
        d1 = abs(p1[0] - p2[0])
        d2 = abs(p1[1] - p2[1])
        return max(d1, d2)
