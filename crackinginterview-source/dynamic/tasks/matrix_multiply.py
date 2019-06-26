import numpy as np
import sys


class MatrixMultiply:

    def simple_matrix_multiply(self, a, b):
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

    def count_minimum_multiplications_recursion(self, p):
        return self.calculate_minimum_multiplication_in_bounds(p, 1, len(p) - 1)

    def count_minimum_multiplications(self,p):
        m, s = self.build_matrix_chain_order(p)
        return m[0][len(p) - 2], self.build_parens(s)

    def calculate_minimum_multiplication_in_bounds(self, p, i, j):
        if i == j:
            return 0
        result = sys.maxsize
        for k in range(i, j):
            prev_min = self.calculate_minimum_multiplication_in_bounds(p, i, k)
            follow_min = self.calculate_minimum_multiplication_in_bounds(p, k+1, j)
            result = min(
                result,
                prev_min + follow_min + (p[i-1] * p[k] * p[j])
            )
        return result

    def build_matrix_chain_order(self, p):
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

    def build_parens(self, s):
        return self.build_parens_in_bounds(s, 0, s.shape[0], "")

    def build_parens_in_bounds(self, s, i, j, res):
        if i == j:
            return res + "A{}".format(i)
        else:
            k = int(s[i,j])
            return '({}{}{})'.format(
                self.build_parens_in_bounds(s, i, k-1, res),
                res,
                self.build_parens_in_bounds(s, k, j,res)
            )

    def matrix_chain_multiply(self, A):
        p = self.build_matrix_dimensions(A)
        m,s = self.build_matrix_chain_order(p)
        res = self.matrix_chain_multiply_in_bounds(A, s, 0, len(A) - 1)
        return res

    def matrix_chain_multiply_in_bounds(self, A, s, i, j):
        if i == j:
            return A[i]
        if i == j - 1:
            return self.simple_matrix_multiply(A[i], A[j])
        else:
            k = int(s[i,j])
            return self.simple_matrix_multiply(
                self.matrix_chain_multiply_in_bounds(A, s, i, k-1),
                self.matrix_chain_multiply_in_bounds(A, s, k, j)
            )

    def build_matrix_dimensions(self, A):
        dimensions = list(map(lambda a: a.shape[0], A))
        dimensions.append(A[len(A) - 1].shape[1])
        return dimensions



