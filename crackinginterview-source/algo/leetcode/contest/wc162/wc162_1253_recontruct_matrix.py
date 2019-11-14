class ReconstructMatrix:

    def reconstruct_matrix(self, upper, lower, colsum):
        if upper + lower != sum(colsum):
            return []
        u, l = [0] * len(colsum), [0] * len(colsum)
        for i in range(len(colsum)):
            if colsum[i] == 2:
                u[i], l[i] = 1, 1
                upper -= 1
                lower -= 1
            elif colsum[i] == 1:
                if upper > lower:
                    u[i], l[i] = 1, 0
                    upper -= 1
                else:
                    u[i], l[i] = 0, 1
                    lower -= 1
            else:
                u[i], l[i] = 0, 0
        if upper != 0 or lower != 0:
            return []
        return [u, l]
