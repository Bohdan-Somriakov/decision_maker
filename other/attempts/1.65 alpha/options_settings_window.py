import tkinter as tk
from analyse_matrix_folder.matrix_calculations import less_than_ten
from making_entries.create_options_entry import create_change_options
from options_matrices import create_options_matrices

def extract_options_number(options_size_entry):
    return int(options_size_entry.get())

def extract_and_create_change_options(options_size_entry, matrices_window, criteria_entries_list, priority_vectors, input_matrix_size_btn):
    input_matrix_size_btn.configure(state=tk.DISABLED)
    options_entries = []
    options_entries_list = []

    create_change_options(matrices_window, extract_options_number(options_size_entry), options_entries_list, options_entries)

    options_btn = tk.Button(matrices_window, text='Apply Changes', command=lambda: create_options_matrices(options_entries_list, options_entries, criteria_entries_list, priority_vectors, options_btn), bg='#3498db', fg='#ffffff', font=('Helvetica', 12, 'bold'))
    options_btn.pack(pady=10)

def options_entry_btn_label(window, criteria_entries_list, priority_vectors):
    input_matrix_size_label = tk.Label(window, text='Enter the Number of Options', font=('Helvetica', 14, 'bold'))
    input_matrix_size_label.pack()

    options_size_entry = tk.Entry(window, width=5, font=('Helvetica', 12))
    options_size_entry.pack()

    input_matrix_size_btn = tk.Button(window, text='Submit', command=lambda: extract_and_create_change_options(options_size_entry, window, criteria_entries_list, priority_vectors, input_matrix_size_btn), bg='#27ae60', fg='#ffffff', font=('Helvetica', 12, 'bold'))
    input_matrix_size_btn.pack(pady=10)

def try_create_options_settings_window(coherence_index_percent, analyse_frame, criteria_entries_list, priority_vectors):
    if less_than_ten(coherence_index_percent):
        options_window = tk.Toplevel()
        options_window.title('Options Settings')
        options_window.geometry('400x300')

        options_entry_btn_label(options_window, criteria_entries_list, priority_vectors)

    else:
        fail = tk.Label(analyse_frame, text='Coherence Index Percent cannot be more than 10%', fg='#e74c3c', font=('Helvetica', 12))
        fail.pack(side='left', padx=10)
