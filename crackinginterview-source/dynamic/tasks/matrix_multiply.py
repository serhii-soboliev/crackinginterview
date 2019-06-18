import numpy as np


class MatrixMultiply:

    @staticmethod
    def simple_matrix_multiply(a, b):
        assert np.shape(a)[1] == np.shape(b)[0], 'Number of matrix A columns should be equal to number of matrix B rows'
        n = np.shape(a)[0]
        m = np.shape(b)[1]
        l = np.shape(a)[1]
        result = np.zeros((n, m))
        for i in range(0,n):
            for j in range(0,m):
                for k in range(0,l):
                    result[i][j] += a[i][k] * b[k][j]
        return result

