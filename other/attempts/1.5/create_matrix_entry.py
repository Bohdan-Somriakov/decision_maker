import tkinter as tk
def create_labels_row(matrix_size, matrix_frame):
    for i in range(matrix_size):
        label = tk.Label(matrix_frame, text=f"Criterion {i}")
        label.grid(row=i + 1, column=0)
def create_lables_column(matrix_size, matrix_frame):
    for j in range(matrix_size):
        label = tk.Label(matrix_frame, text=f"Criterion {j}")
        label.grid(row=0, column=j + 1)
def create_entry_widget(matrix_size, matrix_frame, entries):
    for i in range(matrix_size):
        row_entries = []
        for j in range(matrix_size):
            entry = tk.Entry(matrix_frame, width=3)
            entry.grid(row=i + 1, column=j + 1)
            row_entries.append(entry)
        entries.append(row_entries)
def get_input(entries, matrix):
    print(matrix)
    print(entries)
    for i, row_entries in enumerate(entries):
        for j, entry in enumerate(row_entries):
            entry_value = entry.get()
            if entry_value:
                matrix[i][j] = float(entry_value)
            else:
                matrix[i][j] = 0.0
    print(matrix)
def create_matrix_entry(root, matrix_size, entries, matrix):
    matrix_frame = tk.Frame(root)
    matrix_frame.pack(side="top")
    create_labels_row(matrix_size, matrix_frame)
    create_lables_column(matrix_size, matrix_frame)
    create_entry_widget(matrix_size, matrix_frame, entries)
    get_input(entries, matrix)
