import tkinter as tk
import numpy as np

from analyse_matrix import analyse_matrix
from create_matrix_entry import create_matrix_entry

entries = []
def make_matrix_based_on_size(matrix_size_entry, root, entries):
    matrix_size = int(matrix_size_entry.get())
    matrix = np.zeros((matrix_size, matrix_size))
    return (matrix, matrix_size)
def main_submit(matrix_size_entry, root, entries):
    entries.clear()
    matrix, matrix_size = make_matrix_based_on_size(matrix_size_entry, root, entries)
    create_matrix_entry(root, matrix_size, entries, matrix)
    submit_input_btn(root, matrix)
def main_entry_btn_label(root):
    input_matrix_size_label = tk.Label(root, text='Enter the size of the matrix').pack()
    matrix_size_entry = tk.Entry(root, width=5)
    matrix_size_entry.pack()
    input_matrix_size_btn = tk.Button(root, text='submit',
                                      command=lambda: main_submit(matrix_size_entry, root, entries))
    input_matrix_size_btn.pack(pady=10)
def submit_input_btn(root, matrix):
    button = tk.Button(root, text='Get results', command=lambda: analyse_matrix(root,  entries, matrix))
    button.pack(pady=10)