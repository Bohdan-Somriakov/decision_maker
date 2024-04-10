import numpy as np
from math import prod

def sum_of_columns(matrix):
    column_sums = np.sum(matrix, axis=0)
    return tuple(column_sums)


def calculate_lambda_max_sum(lambda_max):
    return sum(lambda_max)


def calculate_coherence_index(lambda_max_sum, matrix: np.ndarray):
    return (lambda_max_sum - matrix.shape[0])/(matrix.shape[0]-1)


def calculate_coherence_index_percent(coherence_index, matrix: np.ndarray):
    random_consistency_index = {1: 1,
                                2: 1,
                                3: 0.58,
                                4: 0.9,
                                5: 1.12,
                                6: 1.12,
                                7: 1.32,
                                8: 1.41,
                                9: 1.45,
                                10: 1.49}
    return (coherence_index/random_consistency_index[matrix.shape[0]])*100


def calculate_lambda_max(sums, priority_vector):
    lambda_max = list()
    for i in range(len(sums)):
        lambda_max.append(sums[i]*priority_vector[i])
    return tuple(lambda_max)


def calculate_priority_vector(eigenvector):
    priority_vector = [element / eigenvector[-1] for element in eigenvector[:-1]]
    priority_vector.append(sum(priority_vector))
    return tuple(priority_vector)


def calculate_eigenvector(matrix, sums):
    rows_sums = np.product(matrix, axis=1)
    eigenvector = []
    for i in range(matrix.shape[0]):
        eigenvector.append(pow(rows_sums[i], 1 / matrix.shape[0]))
    eigenvector.append(pow(prod(sums), 1 / matrix.shape[0]))
    return tuple(eigenvector)

def less_than_ten(coherence_index_percent):
    return coherence_index_percent < 10