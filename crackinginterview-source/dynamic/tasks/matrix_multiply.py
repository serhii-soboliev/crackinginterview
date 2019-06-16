import numpy as np


class MatrixMultiply:

    @staticmethod
    def simple_matrix_multiply(a, b):
        assert np.shape(a)[1] == np.shape(b)[0], 'Number of matrix A columns should be equal to number of matrix B rows'
        result = np.zeros((np.shape(a)[0], np.shape(b)[1]))
        return result

