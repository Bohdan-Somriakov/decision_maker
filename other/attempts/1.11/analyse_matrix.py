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
    print(type(sums))
    display_sum(matrix.shape[0], root, sums)
    print(matrix)
def sum_of_columns(matrix):
    column_sums = np.sum(matrix, axis=0)
    return tuple(column_sums)

def display_sum(n, root, sums):
    label = tk.Label(root, text='Sum:          ').pack(side='left')
    for i in range(0, n):
        label = tk.Label(root, text=f"{sums[i]}")
        label.pack(side='left', padx=19.5)