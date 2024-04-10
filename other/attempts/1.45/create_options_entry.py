import tkinter as tk

from analyse_matrix_folder.extract_input import extract_criteria_input



def create_change_options(window, matrix_size, options_entries_list, options_entries):
    change_options_frame = tk.Frame(window)
    change_options_frame.pack(side='top')
    create_options_entries(change_options_frame, matrix_size, options_entries_list, options_entries)
    create_options_labels(change_options_frame, matrix_size)


def create_options_entries(change_options_frame, matrix_size, options_entries_list, options_entries):
    for i in range(matrix_size):
        options_entry = tk.Entry(change_options_frame, width=15)
        options_entry.insert(0, f'Criterion {i}')
        options_entry.grid(row=i, column=1)
        options_entries.append(options_entry)
    extract_criteria_input(options_entries_list, options_entries) #probably should work with options as well
    #changes to options_entries_list will be saved


def create_options_labels(change_options_frame, matrix_size):
    for i in range(matrix_size):
        options_label = tk.Label(change_options_frame, text=f'Enter the Options {i} name:')
        options_label.grid(row=i, column=0)
def fill_options_entries_list_default(matrix, options_entries_list):
    if len(options_entries_list) == 0:
        for i in range(matrix.shape[0]):
            options_entries_list.append(f'Option {i}')