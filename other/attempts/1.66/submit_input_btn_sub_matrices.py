import tkinter as tk

def submit_input_btn_sub_matrix(matrices_window, matrix, entries, criteria_entries_list, priority_vectors):
    from analyse_matrix_folder.analyse_matrix import analyse_matrix
    analyse_frame = tk.Frame(matrices_window)
    analyse_frame.pack(side='top')

    button = tk.Button(matrices_window, text='Get Results', command=lambda: analyse_matrix(analyse_frame, entries, matrix, criteria_entries_list, priority_vectors),
                       bg='#3498db', fg='#ffffff', font=('Helvetica', 12, 'bold'))

    button.pack(side='top', pady=10)
