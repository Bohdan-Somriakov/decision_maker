import tkinter as tk
from analyse_matrix_folder.matrix_calculations import less_than_ten
from create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix


def try_create_matrices_window(coherence_index_percent, analyse_frame, criteria_entries_list):
    if (less_than_ten(coherence_index_percent)):
        matrices_window = tk.Toplevel()
        matrices_window.title('matrices')

        sub_matrix = make_matrix_based_on_given_size(len(criteria_entries_list))
        sub_entries = []

        create_matrix_entry(matrices_window, len(criteria_entries_list), sub_entries, sub_matrix)
        submit_input_btn_sub_matrix(matrices_window, sub_matrix, sub_entries, criteria_entries_list)
    else:
        fail = tk.Label(analyse_frame, text='coherence_index_percent cannot be more than 10%', fg='red')
        fail.pack(side='left')