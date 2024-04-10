import tkinter as tk
def create_labels_row(entries_size, matrix_frame):
    for i in range(entries_size):
        label = tk.Label(matrix_frame, text=f"Row {i}")
        label.grid(row=i + 1, column=0)
def create_lables_column(entries_size, matrix_frame):
    for j in range(entries_size):
        label = tk.Label(matrix_frame, text=f"Column {j}")
        label.grid(row=0, column=j + 1)
def create_entry_widget(entries_size, matrix_frame, entries):
    for i in range(entries_size):
        row_entries = []
        for j in range(entries_size):
            entry = tk.Entry(matrix_frame, width=3)
            entry.grid(row=i + 1, column=j + 1)
            row_entries.append(entry)
        entries.append(row_entries)
def get_input(entries, matrix):
    for i, row_entries in enumerate(entries):
        for j, entry in enumerate(row_entries):
            entry_value = entry.get()
            if entry_value:
                matrix[i][j] = float(entry_value)
            else:
                matrix[i][j] = 0.0
    print(matrix)
