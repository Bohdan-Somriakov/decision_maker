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
    display_eigenvector(eigenvector, root)
def sum_of_columns(matrix):
    column_sums = np.sum(matrix, axis=0)
    return tuple(column_sums)

def display_sum(n, root, sums):
    sum_frame = tk.Frame(root)
    sum_frame.pack(side='left')
    label_sum = tk.Label(sum_frame, text='Sum:' + 8*' ')
    label_sum.grid(row=0, column=0)

    for i in range(n):
        label = tk.Label(sum_frame, text=f"{sums[i]}", width=8)
        label.grid(row=0, column=i + 1)
def calculate_eigenvector(matrix):
    rows_sums = np.product(matrix, axis=1)
    eigenvector = []
    for i in range(matrix.shape[0]):
        eigenvector.append(pow(rows_sums[i], 1 / matrix.shape[0]))
    print(eigenvector)
    return tuple(eigenvector)
def display_eigenvector(eigenvector, root):
    eigenvector_frame = tk.Frame(root)
    eigenvector_frame.pack(side='left')
    eigenvector_label = tk.Label(eigenvector_frame, text='eigenvector', width=10)
    eigenvector_label.grid(row=0, column=0)
    for i in range(len(eigenvector)):
        print(eigenvector[i])
        label_eigenvector_elem = tk.Label(eigenvector_frame, text=f'{round(eigenvector[i], 2):.2f}', width=8)

        label_eigenvector_elem.grid(row=i+1, column=0)


