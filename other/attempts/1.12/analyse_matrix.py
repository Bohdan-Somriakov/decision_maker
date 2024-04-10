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
    print(matrix)
def sum_of_columns(matrix):
    column_sums = np.sum(matrix, axis=0)
    return tuple(column_sums)

def display_sum(n, root, sums):
    sum_frame = tk.Frame(root)
    sum_frame.pack(side='left')
    label_sum = tk.Label(sum_frame, text='Sum:' + 8*' ')
    label_sum.grid(row=0, column=0, sticky='w')

    for i in range(n):
        label = tk.Label(sum_frame, text=f"{sums[i]}", width=8)
        label.grid(row=0, column=i + 1)

