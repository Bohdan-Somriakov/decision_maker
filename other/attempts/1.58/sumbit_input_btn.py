import tkinter as tk

from analyse_matrix_folder.analyse_matrix import analyse_matrix_make_window


def submit_input_btn(root, matrix, entries, criteria_entries_list):
    analyse_frame = tk.Frame(root)
    analyse_frame.pack(padx=10, pady=10)
    priority_vectors = list()
    button = tk.Button(root, text='Get results', command=lambda: analyse_matrix_make_window(analyse_frame,
                                                                                entries, matrix,
                                                                                criteria_entries_list,
                                                                                priority_vectors))
    button.pack(pady=10)



