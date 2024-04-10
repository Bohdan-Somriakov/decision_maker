import numpy as np
from math import prod

def sum_of_columns(matrix):
    try:
        column_sums = np.sum(matrix, axis=0)
        return tuple(column_sums)
    except Exception as e:
        print(f"Exception in sum_of_columns with params: matrix={matrix}, Error: {e}")
        return ()

def calculate_lambda_max_sum(lambda_max):
    try:
        return sum(lambda_max)
    except Exception as e:
        print(f"Exception in calculate_lambda_max_sum with params: lambda_max={lambda_max}, Error: {e}")
        return 0

def calculate_coherence_index(lambda_max_sum, matrix):
    try:
        if matrix.shape[0] <= 1:
            return 0
        return (lambda_max_sum - matrix.shape[0]) / (matrix.shape[0] - 1)
    except Exception as e:
        print(f"Exception in calculate_coherence_index with params: lambda_max_sum={lambda_max_sum}, matrix={matrix}, Error: {e}")
        return 0

def calculate_coherence_index_percent(coherence_index, matrix):
    try:
        if matrix.shape[0] not in range(1, 11):
            return 0
        random_consistency_index = {1: 1, 2: 1, 3: 0.58, 4: 0.9, 5: 1.12, 6: 1.12, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
        return (coherence_index / random_consistency_index[matrix.shape[0]]) * 100
    except Exception as e:
        print(f"Exception in calculate_coherence_index_percent with params: coherence_index={coherence_index}, matrix={matrix}, Error: {e}")
        return 0

def calculate_lambda_max(sums, priority_vector):
    try:
        lambda_max = [sums[i] * priority_vector[i] for i in range(len(sums))]
        return tuple(lambda_max)
    except Exception as e:
        print(f"Exception in calculate_lambda_max with params: sums={sums}, priority_vector={priority_vector}, Error: {e}")
        return ()

def calculate_priority_vector(eigenvector):
    try:
        if eigenvector[-1] == 0:
            return ()
        priority_vector = [element / eigenvector[-1] for element in eigenvector[:-1]]
        priority_vector.append(sum(priority_vector))
        return tuple(priority_vector)
    except Exception as e:
        print(f"Exception in calculate_priority_vector with params: eigenvector={eigenvector}, Error: {e}")
        return ()

def calculate_eigenvector(matrix):
    try:
        rows_sums = np.product(matrix, axis=1)
        eigenvector = [pow(rows_sums[i], 1 / matrix.shape[0]) for i in range(matrix.shape[0])]
        eigenvector.append(sum(eigenvector))
        return tuple(eigenvector)
    except Exception as e:
        print(f"Exception in calculate_eigenvector with params: matrix={matrix}, Error: {e}")
        return ()

def less_than_ten(coherence_index_percent):
    try:
        return coherence_index_percent < 10
    except Exception as e:
        print(f"Exception in less_than_ten with params: coherence_index_percent={coherence_index_percent}, Error: {e}")
        return False
