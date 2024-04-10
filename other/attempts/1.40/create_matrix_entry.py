import tkinter as tk

from analyse_matrix_folder.extract_input import extract_input


def create_labels_row(matrix_size, matrix_frame, label_names=()):
    if not label_names:
        label_names = [f"Criterion {i}" for i in range(1, matrix_size + 1)]

    for i, label_name in enumerate(label_names):
        label = tk.Label(matrix_frame, text=label_name)
        label.grid(row=i + 1, column=0)


def create_labels_column(matrix_size, matrix_frame, label_names=()):
    if not label_names:
        label_names = [f"Criterion {j}" for j in range(1, matrix_size + 1)]

    for j, label_name in enumerate(label_names):
        label = tk.Label(matrix_frame, text=label_name)
        label.grid(row=0, column=j + 1)


def create_entry_widget(matrix_size, matrix_frame, entries):
    for i in range(matrix_size):
        row_entries = []
        for j in range(matrix_size):
            entry = tk.Entry(matrix_frame, width=3)
            entry.grid(row=i + 1, column=j + 1)
            if i == j:
                entry.insert(0,'1')
            row_entries.append(entry)
        entries.append(row_entries)



def create_matrix_entry(matrix_frame, matrix_size, entries, matrix):
    create_labels_row(matrix_size, matrix_frame)
    create_labels_column(matrix_size, matrix_frame)
    create_entry_widget(matrix_size, matrix_frame, entries)
    extract_input(entries, matrix)
