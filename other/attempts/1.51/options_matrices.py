from analyse_matrix_folder.extract_input import extract_criteria_input
import tkinter as tk

from making_entries.create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix


def create_options_matrices(options_entries_list, options_entries, criteria_entries_list):

    extract_criteria_input(options_entries_list, options_entries)

    matrices_window =tk.Toplevel()
    matrices_window.title('matrices')

    sub_matrix = make_matrix_based_on_given_size(len(criteria_entries_list))

    matrix_frame = tk.Frame(matrices_window)
    matrix_frame.pack(padx='10')

    sub_entries = []
    create_matrix_entry(matrix_frame, len(criteria_entries_list), sub_entries, sub_matrix, options_entries_list)

    submit_input_btn_sub_matrix(matrices_window, sub_matrix, sub_entries, criteria_entries_list)
