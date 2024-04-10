from analyse_matrix_folder.extract_input import extract_criteria_input
import tkinter as tk

from making_entries.create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix


def create_options_matrices(options_entries_list, options_entries, criteria_entries_list):

    extract_criteria_input(options_entries_list, options_entries)

    matrices_window = tk.Toplevel()
    matrices_window.title('matrices')

    print(criteria_entries_list)

    for i, elem in enumerate(criteria_entries_list):

        matrix_frame_and_btn = tk.Frame(matrices_window)
        matrix_frame_and_btn.pack(side='left')

        matrix_frame = tk.Frame(matrix_frame_and_btn)
        matrix_frame.pack(side='top')

        sub_matrix = make_matrix_based_on_given_size(len(options_entries))

        sub_entries = []
        create_matrix_entry(matrix_frame, len(options_entries), sub_entries, sub_matrix, options_entries_list)

        submit_input_btn_sub_matrix(matrix_frame_and_btn, sub_matrix, sub_entries, criteria_entries_list)


