import tkinter as tk
import numpy as np

from analyse_matrix_folder.analyse_matrix import analyse_matrix
from analyse_matrix_folder.extract_input import extract_criteria_input
from create_criteria_entry import create_change_criteria
from create_matrix_entry import create_matrix_entry
from show_hide_label import show_label

entries = [] #matrix entries
criteria_entries_list = []
def make_matrix_based_on_size(matrix_size_entry, root, entries):
    matrix_size = int(matrix_size_entry.get())
    matrix = np.zeros((matrix_size, matrix_size))
    return matrix, matrix_size

def create_criteria_btn(criteria_entries_list, root, matrix_frame):
    criteria_btn = tk.Button(root, text='Apply changes')
    criteria_btn.pack(pady=10)


def main_submit(matrix_size_entry, root, entries):
    entries.clear()
    matrix, matrix_size = make_matrix_based_on_size(matrix_size_entry, root, entries)
    matrix_frame = tk.Frame(root)
    matrix_frame.pack(side="top")
    if 0 < matrix_size < 11:
        create_matrix_entry(matrix_frame, matrix_size, entries, matrix)
        submit_input_btn(root, matrix)
        create_change_criteria(root, matrix_size, criteria_entries_list)
        create_criteria_btn(criteria_entries_list, root, matrix_frame)
    else:
        error_label = tk.Label(root, text='0 < matrix_size < 11', fg='red')
        show_label(error_label)


def main_entry_btn_label(root):
    input_matrix_size_label = tk.Label(root, text='Enter the size of the matrix').pack()
    matrix_size_entry = tk.Entry(root, width=5)
    matrix_size_entry.pack()
    input_matrix_size_btn = tk.Button(root, text='submit',
                                      command=lambda: main_submit(matrix_size_entry, root, entries))
    input_matrix_size_btn.pack(pady=10)


def submit_input_btn(root, matrix):
    analyse_frame = tk.Frame(root)
    analyse_frame.pack(padx=10, pady=10)
    button = tk.Button(root, text='Get results', command=lambda: analyse_matrix(analyse_frame,  entries, matrix))
    button.pack(pady=10)