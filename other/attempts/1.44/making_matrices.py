import numpy as np
def make_matrix_based_on_size(matrix_size_entry, root, entries):
    matrix_size = int(matrix_size_entry.get())
    matrix = np.zeros((matrix_size, matrix_size))
    return matrix, matrix_size


def make_matrix_based_on_given_size(matrix_size):
    matrix = np.zeros((matrix_size, matrix_size))
    return matrix
