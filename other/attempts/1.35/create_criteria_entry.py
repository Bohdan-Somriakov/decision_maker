import tkinter as tk

from analyse_matrix_folder.extract_input import extract_criteria_input



def create_change_criteria(root, matrix_size, criteria_entries_list, criteria_entries):
    change_criteria_frame = tk.Frame(root)
    change_criteria_frame.pack(side='top')
    create_criteria_entries(change_criteria_frame, matrix_size, criteria_entries_list, criteria_entries)
    create_criteria_labels(change_criteria_frame, matrix_size)


def create_criteria_entries(change_criteria_frame, matrix_size, criteria_entries_list, criteria_entries):
    for i in range(matrix_size):
        criteria_entry = tk.Entry(change_criteria_frame, width=15)
        criteria_entry.insert(0, f'Criterion {i}')
        criteria_entry.grid(row=i, column=1)
        criteria_entries.append(criteria_entry)
    extract_criteria_input(criteria_entries_list, criteria_entries)
    #changes to criteria_entries_list will be saved


def create_criteria_labels(change_criteria_frame, matrix_size):
    for i in range(matrix_size):
        criteria_label = tk.Label(change_criteria_frame, text=f'Enter the Criterion {i} name:')
        criteria_label.grid(row=i, column=0)

