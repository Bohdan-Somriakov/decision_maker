import tkinter as tk
from analyse_matrix_folder.extract_input import extract_criteria_input

def create_change_options(window, matrix_size, options_entries_list, options_entries):
    change_options_frame = tk.Frame(window, bg='#f0f0f0', pady=10, padx=15, borderwidth=2, relief='ridge')  # Set background color, padding, border, and relief
    change_options_frame.pack(side='top', pady=10)
    create_options_entries(change_options_frame, matrix_size, options_entries_list, options_entries)
    create_options_labels(change_options_frame, matrix_size)

def create_options_entries(change_options_frame, matrix_size, options_entries_list, options_entries):
    for i in range(matrix_size):
        options_entry = tk.Entry(change_options_frame, width=20, fg='#3498db', font=('Arial', 10))  # Change text color to blue, set font, and increase width
        options_entry.insert(0, f'Option {i}')
        options_entry.grid(row=i, column=1, pady=5)
        options_entries.append(options_entry)
    extract_criteria_input(options_entries_list, options_entries)  # changes to options_entries_list will be saved

def create_options_labels(change_options_frame, matrix_size):
    for i in range(matrix_size):
        options_label = tk.Label(change_options_frame, text=f'Enter the Option {i} name:', fg='#27ae60', font=('Arial', 10, 'bold'))  # Change text color to green, set font, and make it bold
        options_label.grid(row=i, column=0, pady=5)

def fill_options_entries_list_default(matrix, options_entries_list):
    if len(options_entries_list) == 0:
        for i in range(matrix.shape[0]):
            options_entries_list.append(f'Option {i}')
