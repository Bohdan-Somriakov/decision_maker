import tkinter as tk
from analyse_matrix_folder.extract_input import extract_criteria_input

def create_change_criteria(root, matrix_size, criteria_entries_list, criteria_entries):
    change_criteria_frame = tk.Frame(root, bg='#F2EBE5', pady=10, padx=15, borderwidth=2, relief='ridge')
    change_criteria_frame.pack(side='top', pady=10)
    create_criteria_entries(change_criteria_frame, matrix_size, criteria_entries_list, criteria_entries)
    create_criteria_labels(change_criteria_frame, matrix_size)

def create_criteria_entries(change_criteria_frame, matrix_size, criteria_entries_list, criteria_entries):
    for i in range(matrix_size):
        criteria_entry = tk.Entry(change_criteria_frame, width=20, bg='#647295', fg='white', font=('Arial', 10))
        criteria_entry.insert(0, f'Criterion {i}')
        criteria_entry.grid(row=i, column=1, pady=5)
        criteria_entries.append(criteria_entry)
    extract_criteria_input(criteria_entries_list, criteria_entries)

def create_criteria_labels(change_criteria_frame, matrix_size):
    change_criteria_frame.config(bg='#9F496E')
    for i in range(matrix_size):
        criteria_label = tk.Label(change_criteria_frame, text=f'Enter the Criterion {i} name:', fg='#2B262D', font=('Arial', 10, 'bold'))
        criteria_label.grid(row=i, column=0, pady=5)

def fill_criteria_entries_list_default(matrix, criteria_entries_list):
    if len(criteria_entries_list) == 0:
        for i in range(matrix.shape[0]):
            criteria_entries_list.append(f'Criterion {i}')