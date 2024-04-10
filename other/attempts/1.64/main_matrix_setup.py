import tkinter as tk

from analyse_matrix_folder.extract_input import extract_criteria_input
from making_entries.create_criteria_entry import create_change_criteria
from making_entries.create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_size
from show_hide_label import show_label
from sumbit_input_btn import submit_input_btn

entries = [] #matrix entries
criteria_entries_list = []

def rename_criteria(matrix_frame, criteria_entries_list, criteria_entries):
    extract_criteria_input(criteria_entries_list, criteria_entries)
    labels_list = list()

    for child in matrix_frame.winfo_children():
        if isinstance(child, tk.Label):
            labels_list.append(child)
    for i, label in enumerate(labels_list):
        if i < len(labels_list)/2:
            label.config(text=f'{criteria_entries_list[i]}')
        else:
            label.config(text=f'{criteria_entries_list[i-int(len(labels_list)/2)]}')


def create_criteria_btn(criteria_entries_list, root, matrix_frame, criteria_entries):
    criteria_entries_list.clear()
    criteria_btn = tk.Button(root, text='Apply changes', command=lambda: rename_criteria(matrix_frame, criteria_entries_list, criteria_entries))
    criteria_btn.pack(pady=10)


def main_submit(matrix_size_entry, root, entries, input_matrix_size_btn):
    input_matrix_size_btn.configure(state=tk.DISABLED)
    entries.clear()
    matrix, matrix_size = make_matrix_based_on_size(matrix_size_entry, root, entries)
    matrix_frame = tk.Frame(root)
    matrix_frame.pack(side="top")
    if 1 < matrix_size < 11:
        create_matrix_entry(matrix_frame, matrix_size, entries, matrix)
        submit_input_btn(root, matrix, entries, criteria_entries_list)
        criteria_entries = []
        create_change_criteria(root, matrix_size, criteria_entries_list, criteria_entries)
        create_criteria_btn(criteria_entries_list, root, matrix_frame, criteria_entries)
    else:
        error_label = tk.Label(root, text='1 < matrix_size < 11', fg='red')
        show_label(error_label)


def main_entry_btn_label(root):
    input_matrix_size_label = tk.Label(root, text='Enter the size of the matrix').pack()
    matrix_size_entry = tk.Entry(root, width=5)
    matrix_size_entry.pack()
    input_matrix_size_btn = tk.Button(root, text='Submit',
                                      command=lambda: main_submit(matrix_size_entry, root, entries, input_matrix_size_btn))
    input_matrix_size_btn.pack(pady=10)



