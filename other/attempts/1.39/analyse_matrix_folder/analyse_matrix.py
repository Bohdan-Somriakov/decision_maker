import tkinter as tk

import numpy as np

from analyse_matrix_folder.extract_input import extract_input
from analyse_matrix_folder.matrix_calculations import (
    sum_of_columns,
    calculate_eigenvector,
    calculate_priority_vector,
    calculate_lambda_max,
    calculate_lambda_max_sum,
    calculate_coherence_index,
    calculate_coherence_index_percent,
    less_than_ten
)

from analyse_matrix_folder.matrix_display_calculations import (
    display_sum,
    display_eigenvector_and_priority_vector,
    display_lambda_max,
    display_lambda_max_sum,
    display_coherence_index,
    display_coherence_index_percent
)
from clean_frame import clean_frame
from create_criteria_entry import fill_criteria_entries_list_default
from create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_given_size


def analyse_matrix(analyse_frame, entries, matrix, criteria_entries_list):
    clean_frame(analyse_frame)
    extract_input(entries, matrix)  # changes to matrix will be saved
    sums = ()
    sums = sum_of_columns(matrix)
    display_sum(matrix.shape[0], analyse_frame, sums)
    eigenvector = ()
    eigenvector = calculate_eigenvector(matrix)
    priority_vector = ()
    priority_vector = calculate_priority_vector(eigenvector)
    display_eigenvector_and_priority_vector(eigenvector, priority_vector, analyse_frame)
    lambda_max = ()
    lambda_max = calculate_lambda_max(sums, priority_vector)
    display_lambda_max(lambda_max, analyse_frame)
    lambda_max_sum = 0
    lambda_max_sum = calculate_lambda_max_sum(lambda_max)
    display_lambda_max_sum(lambda_max_sum, analyse_frame)
    coherence_index = 0
    coherence_index = calculate_coherence_index(lambda_max_sum, matrix)
    display_coherence_index(coherence_index, analyse_frame)
    coherence_index_percent = calculate_coherence_index_percent(coherence_index, matrix)
    display_coherence_index_percent(coherence_index_percent, analyse_frame)

    fill_criteria_entries_list_default(matrix, criteria_entries_list)

    try_create_matrices_window(coherence_index_percent, analyse_frame, criteria_entries_list)


def try_create_matrices_window(coherence_index_percent, analyse_frame, criteria_entries_list):
    if (less_than_ten(coherence_index_percent)):
        matrices_window = tk.Toplevel()
        matrices_window.title('matrices')

        sub_matrix = make_matrix_based_on_given_size(len(criteria_entries_list))
        su_entries = []

        create_matrix_entry(matrices_window, len(criteria_entries_list), su_entries, sub_matrix)
    else:
        fail = tk.Label(analyse_frame, text='coherence_index_percent cannot be more than 10%', fg='red')
        fail.pack(side='left')

