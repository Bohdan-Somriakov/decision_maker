import tkinter as tk

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
from create_criteria_entry import fill_criteria_entries_list_default
from options_settings_window import try_create_options_settings_window


def analyse_matrix_make_window(analyse_frame, entries, matrix, criteria_entries_list):
    coherence_index_percent = analyse_matrix(analyse_frame, entries, matrix, criteria_entries_list)
    try_create_options_settings_window(coherence_index_percent, analyse_frame, criteria_entries_list)


def analyse_matrix(analyse_frame, entries, matrix, criteria_entries_list):
    clean_frame(analyse_frame)
    extract_input(entries, matrix)  # changes to matrix will be saved
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
