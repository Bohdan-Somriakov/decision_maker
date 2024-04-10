from analyse_matrix_folder.extract_input import extract_criteria_input
import tkinter as tk

from making_entries.create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix

def make_sub_matrix_setup(matrices_window, options_entries, options_entries_list, criteria_entries_list, priority_vectors):
    matrix_frame_and_btn = tk.Frame(matrices_window)
    matrix_frame_and_btn.pack(side='left')

    matrix_frame = tk.Frame(matrix_frame_and_btn)
    matrix_frame.pack(side='top')

    sub_matrix = make_matrix_based_on_given_size(len(options_entries))

    sub_entries = []
    create_matrix_entry(matrix_frame, len(options_entries), sub_entries, sub_matrix, options_entries_list)

    submit_input_btn_sub_matrix(matrix_frame_and_btn, sub_matrix, sub_entries, criteria_entries_list, priority_vectors)


def create_options_matrices(options_entries_list, options_entries, criteria_entries_list, priority_vectors):

    extract_criteria_input(options_entries_list, options_entries)

    matrices_window = tk.Toplevel()
    matrices_window.title('matrices')

    print(criteria_entries_list)

    for i, elem in enumerate(criteria_entries_list):
        make_sub_matrix_setup(matrices_window, options_entries, options_entries_list, criteria_entries_list, priority_vectors)

    submit_all_btn = tk.Button(matrices_window, text='submit all',
                               command=lambda: calculate_display_results(priority_vectors))
    submit_all_btn.pack(side='bottom', anchor='center')


def calculate_display_results(priority_vectors):
    print(priority_vectors)


