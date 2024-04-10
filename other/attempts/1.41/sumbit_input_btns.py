import tkinter as tk

from analyse_matrix_folder.analyse_matrix import analyse_matrix


def submit_input_btn(root, matrix, entries, criteria_entries_list):
    analyse_frame = tk.Frame(root)
    analyse_frame.pack(padx=10, pady=10)
    button = tk.Button(root, text='Get results', command=lambda: analyse_matrix(analyse_frame,
                                                                                entries, matrix,
                                                                                criteria_entries_list))
    button.pack(pady=10)

    #try_create_matrices_window(coherence_index_percent, analyse_frame, criteria_entries_list)