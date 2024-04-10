import tkinter as tk
from analyse_matrix_folder.matrix_calculations import less_than_ten
from create_matrix_entry import create_matrix_entry
from create_options_entry import create_change_options
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix


def extract_options_number(options_size_entry):
    return int(options_size_entry.get())


def extract_and_create_change_options(options_size_entry, matrices_window):
    option_entries = []
    option_entries_list = []

    create_change_options(matrices_window,
                          extract_options_number(options_size_entry),
                          option_entries_list, option_entries)
    print(option_entries_list)

def options_entry_btn_label(window):
    input_matrix_size_label = (tk.Label(window, text='Enter the number of options'))
    input_matrix_size_label.pack()
    options_size_entry = tk.Entry(window, width=5)
    options_size_entry.pack()
    input_matrix_size_btn = tk.Button(window, text='submit',
                                      command=lambda: extract_and_create_change_options(options_size_entry,
                                                                                        window))
    input_matrix_size_btn.pack(pady=10)


def try_create_matrices_window(coherence_index_percent, analyse_frame, criteria_entries_list):
    if (less_than_ten(coherence_index_percent)):
        matrices_window = tk.Toplevel()
        matrices_window.title('matrices')

        options_entry_btn_label(matrices_window)

        sub_matrix = make_matrix_based_on_given_size(len(criteria_entries_list))

        #matrix_frame = tk.Frame(matrices_window)
        #matrix_frame.pack(pady='10')
        #create_matrix_entry(matrix_frame, len(criteria_entries_list), sub_entries, sub_matrix)

        #submit_input_btn_sub_matrix(matrices_window, sub_matrix, sub_entries, criteria_entries_list)
    else:
        fail = tk.Label(analyse_frame, text='coherence_index_percent cannot be more than 10%', fg='red')
        fail.pack(side='left')