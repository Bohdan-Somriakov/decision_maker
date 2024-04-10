import tkinter as tk
import numpy as np
def extract_input(entries, matrix):
    for i, row_entries in enumerate(entries):
        for j, entry in enumerate(row_entries):
            entry_value = entry.get()
            if entry_value:
                matrix[i][j] = float(entry_value)
            else:
                matrix[i][j] = 0.0
def analyse_matrix(root,  entries, matrix):
    extract_input(entries, matrix)  # changes to matrix will be saved
    sums = ()
    sums = sum_of_columns(matrix)
    display_sum(matrix.shape[0], root, sums)
    eigenvector = ()
    eigenvector = calculate_eigenvector(matrix)
    priority_vector = ()
    priority_vector = calculate_priority_vector(eigenvector)
    display_eigenvector_and_priority_vector(eigenvector, priority_vector, root)
    lambda_max = ()
    lambda_max = calculate_lambda_max(sums, priority_vector)
    display_lambda_max(lambda_max, root)
    lambda_max_sum = 0
    lambda_max_sum = calculate_lambda_max_sum(lambda_max)
    display_lambda_max_sum(lambda_max_sum, root)
    coherence_index = 0
    coherence_index = calculate_coherence_index(lambda_max_sum, matrix)
    display_coherence_index(coherence_index, root)
    coherence_index_percent = 0
    coherence_index_percent = calculate_coherence_index_percent(coherence_index, matrix)
    display_coherence_index_percent(coherence_index_percent, root)

def sum_of_columns(matrix):
    column_sums = np.sum(matrix, axis=0)
    return tuple(column_sums)

def display_sum(n, root, sums):
    sum_frame = tk.Frame(root)
    sum_frame.pack(side='top')
    label_sum = tk.Label(sum_frame, text='Sum:' + 8*' ')
    label_sum.grid(row=0, column=0)

    for i in range(n):
        label = tk.Label(sum_frame, text=f"{round(sums[i], 2):.2f}", width=8)
        label.grid(row=0, column=i + 1)
def calculate_eigenvector(matrix):
    rows_sums = np.product(matrix, axis=1)
    eigenvector = []
    for i in range(matrix.shape[0]):
        eigenvector.append(pow(rows_sums[i], 1 / matrix.shape[0]))
    eigenvector.append(sum(eigenvector))
    return tuple(eigenvector)
def display_eigenvector_and_priority_vector(eigenvector, priority_vector, root):
    vectors_frame = tk.Frame(root)
    eigenvector_frame = tk.Frame(vectors_frame)
    priority_vector_frame = tk.Frame(vectors_frame)
    vectors_frame.pack(side='top')
    display_eigenvector(eigenvector_frame, eigenvector, root)
    display_priority_vector(priority_vector_frame, priority_vector, root)

def display_eigenvector(eigenvector_frame, eigenvector, root):
    eigenvector_frame.pack(side='left')
    eigenvector_label = tk.Label(eigenvector_frame, text='eigenvector', width=10)
    eigenvector_label.grid(row=0, column=0)
    for i in range(len(eigenvector)):
        label_eigenvector_elem = tk.Label(eigenvector_frame, text=f'{round(eigenvector[i], 2):.2f}', width=8)

        label_eigenvector_elem.grid(row=i+1, column=0)
def calculate_priority_vector(eigenvector):
    priority_vector = [element / eigenvector[-1] for element in eigenvector[:-1]]
    priority_vector.append(sum(priority_vector))
    return tuple(priority_vector)
def display_priority_vector(priority_vector_frame, priority_vector, root):
    priority_vector_frame.pack(side='left')
    eigenvector_label = tk.Label(priority_vector_frame, text='priority vector', width=10)
    eigenvector_label.grid(row=0, column=0)
    for i in range(len(priority_vector)):
        label_eigenvector_elem = tk.Label(priority_vector_frame, text=f'{round(priority_vector[i], 2):.2f}', width=8)

        label_eigenvector_elem.grid(row=i + 1, column=0)
def calculate_lambda_max(sums, priority_vector):
    lambda_max = list()
    for i in range(len(sums)):
        lambda_max.append(sums[i]*priority_vector[i])
    return tuple(lambda_max)
def display_lambda_max(lambda_max, root):
    lambda_max_frame = tk.Frame(root)
    lambda_max_frame.pack(side='top')
    label_lambda_max = tk.Label(lambda_max_frame, text='lambda_max:', pady=10)
    label_lambda_max.grid(row=0, column=0)
    for i in range(len(lambda_max)):
        label_lambda_max = tk.Label(lambda_max_frame, text=f'{round(lambda_max[i], 2):.2f}', width=8)
        label_lambda_max.grid(row=0, column=i+1)
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
def display_coherence_index_percent(coherence_index_percent, root):
    display_variable('coherence_index_percent', coherence_index_percent, root)
def display_coherence_index(coherence_index, root):
    display_variable('coherence_index', coherence_index, root)
def display_lambda_max_sum(lambda_max_sum, root):
    display_variable('coherence_index', lambda_max_sum, root)
def display_variable(frame_title, variable_value, root):
    variable_frame = tk.Frame(root)
    variable_frame.pack(side='top')

    title_label = tk.Label(variable_frame, text=f'{frame_title}:')
    title_label.grid(row=0, column=1)

    value_label = tk.Label(variable_frame, text=f'{round(variable_value, 2):.2f}')
    value_label.grid(row=0, column=2)
