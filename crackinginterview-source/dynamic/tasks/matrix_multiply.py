import numpy as np
import sys



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

    @staticmethod
    def count_minimum_multiplications_recursion(p):
        return MatrixMultiply.calculate_minimum_multiplication_in_bounds(p, 1, len(p) - 1)

    @staticmethod
    def count_minimum_multiplications(p):
        m, s = MatrixMultiply.build_matrix_chain_order(p)
        return m[0][len(p) - 2], MatrixMultiply.build_parens(s)

    @staticmethod
    def calculate_minimum_multiplication_in_bounds(p, i, j):
        if i == j:
            return 0
        result = sys.maxsize
        for k in range(i, j):
            prev_min = MatrixMultiply.calculate_minimum_multiplication_in_bounds(p, i, k)
            follow_min = MatrixMultiply.calculate_minimum_multiplication_in_bounds(p, k+1, j)
            result = min(
                result,
                prev_min + follow_min + (p[i-1] * p[k] * p[j])
            )
        return result

    @staticmethod
    def build_matrix_chain_order(p):
        n = len(p) - 1
        m = np.zeros([n, n])
        s = np.zeros([n-1, n])
        for l in range(2, n+1):
            for i in range(0, n - l + 1):
                j = i + l - 1
                m[i,j] = sys.maxsize
                for k in range(i, j):
                    q = m[i,k] + m[k+1,j] + p[i] * p[k+1] * p[j+1]
                    if q < m[i,j]:
                        m[i,j] = q
                        s[i,j] = k + 1
        return m, s

    @staticmethod
    def build_parens(s):
        return MatrixMultiply.build_parens_in_bounds(s, 0, s.shape[0], "")

    @staticmethod
    def build_parens_in_bounds(s, i, j, res):
        if i == j:
            return res + "A{}".format(i)
        else:
            k = int(s[i,j])
            return '({}{}{})'.format(
                MatrixMultiply.build_parens_in_bounds(s, i, k-1, res),
                res,
                MatrixMultiply.build_parens_in_bounds(s, k, j,res)
            )




