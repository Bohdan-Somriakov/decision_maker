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
from making_entries.create_criteria_entry import fill_criteria_entries_list_default
from options_settings_window import try_create_options_settings_window

def analyse_matrix_make_window(analyse_frame, entries, matrix, criteria_entries_list, priority_vectors):
    coherence_index_percent = analyse_matrix(analyse_frame, entries, matrix, criteria_entries_list, priority_vectors)
    try_create_options_settings_window(coherence_index_percent, analyse_frame, criteria_entries_list, priority_vectors)


def analyse_matrix(analyse_frame, entries, matrix, criteria_entries_list, priority_vectors):
    clean_frame(analyse_frame)
    extract_input(entries, matrix, analyse_frame)  # changes to matrix will be saved
    sums = ()
    sums = sum_of_columns(matrix)
    eigenvector = ()
    eigenvector = calculate_eigenvector(matrix)
    priority_vector = ()
    priority_vector = calculate_priority_vector(eigenvector)
    lambda_max = ()
    lambda_max = calculate_lambda_max(sums, priority_vector)
    lambda_max_sum = 0
    lambda_max_sum = calculate_lambda_max_sum(lambda_max)
    coherence_index = 0
    coherence_index = calculate_coherence_index(lambda_max_sum, matrix)
    coherence_index_percent = calculate_coherence_index_percent(coherence_index, matrix)

    analysed_matrix_display_results(matrix, analyse_frame,
                                        sums, eigenvector, priority_vector,
                                        lambda_max, lambda_max_sum, coherence_index,
                                        coherence_index_percent)
    fill_criteria_entries_list_default(matrix, criteria_entries_list) #only works with empty list

    if np.any(matrix <= 0.1):
        print("Condition: matrix values cannot contain values less than 1/9")
        error_label = tk.Label(analyse_frame, text='matrix values cannot contain values less than 1/9', fg='red')
        error_label.pack(side='top')
        coherence_index_percent = 99999  # just to trigger the error

    elif np.any(matrix > 9):
        print("Condition: matrix values cannot contain values more than 9")
        error_label = tk.Label(analyse_frame, text='matrix values cannot contain values more than 9', fg='red')
        error_label.pack(side='top')
        coherence_index_percent = 99999  # just to trigger the error

    elif np.any(np.isnan(matrix).any()):
        print("Condition: matrix values cannot contain text")
        error_label = tk.Label(analyse_frame, text='matrix values cannot contain text', fg='red')
        error_label.pack(side='top')
        coherence_index_percent = 99999  # just to trigger the error

    elif coherence_index_percent >= 10:
        print("Condition: coherence_index_percent cannot be more than 10")
        error_label = tk.Label(analyse_frame, text='coherence_index_percent cannot be more than 10', fg='red')
        error_label.pack(side='top')
        coherence_index_percent = 99999  # just to trigger the error

    else:
        priority_vectors.append(priority_vector) #we have to collect them for the results
    return coherence_index_percent


def analysed_matrix_display_results(matrix, analyse_frame,
                                   sums, eigenvector, priority_vector,
                                   lambda_max, lambda_max_sum, coherence_index,
                                   coherence_index_percent):
    display_sum(matrix.shape[0], analyse_frame, sums)
    display_eigenvector_and_priority_vector(eigenvector, priority_vector, analyse_frame)
    display_lambda_max(lambda_max, analyse_frame)
    display_lambda_max_sum(lambda_max_sum, analyse_frame)
    display_coherence_index(coherence_index, analyse_frame)
    display_coherence_index_percent(coherence_index_percent, analyse_frame)
