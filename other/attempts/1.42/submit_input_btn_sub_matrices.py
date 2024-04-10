import tkinter as tk


def submit_input_btn_sub_matrix(root, matrix, entries, criteria_entries_list):
    from analyse_matrix_folder.analyse_matrix import analyse_matrix
    analyse_frame = tk.Frame(root)
    analyse_frame.pack(padx=10, pady=10)
    button = tk.Button(root, text='Get results', command=lambda: analyse_matrix(analyse_frame,
                                                                                entries, matrix,
                                                                                criteria_entries_list))
    button.pack(pady=10)
