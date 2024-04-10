import numpy as np
import tkinter as tk

def extract_input(entries, matrix, matrix_frame):
    for i, row_entries in enumerate(entries):
        for j, entry in enumerate(row_entries):
            entry_value = entry.get()
            if entry_value:
                try:
                    entry_value = float(eval(entry_value))
                    matrix[i][j] = entry_value
                except (NameError, TypeError, ValueError):
                    label = tk.Label(matrix_frame, text="Matrix can only contain numbers", fg='red')
                    label.pack(side='top')
                    return
            else:
                matrix[i][j] = 0.0


def extract_criteria_input(criteria_entries_list, criteria_entries):
    criteria_entries_list.clear()
    for entry in criteria_entries:
        entry_value = entry.get()
        criteria_entries_list.append(entry_value)
