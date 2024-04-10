import tkinter as tk
from analyse_matrix_folder.matrix_calculations import less_than_ten
from create_matrix_entry import create_matrix_entry
from create_options_entry import create_change_options
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix


def options_entry_btn_label(root):
    input_matrix_size_label = tk.Label(root, text='Enter the size of the matrix').pack()
    matrix_size_entry = tk.Entry(root, width=5)
    matrix_size_entry.pack()
    #input_matrix_size_btn = tk.Button(root, text='submit',
    #                                  command=lambda: main_submit(matrix_size_entry, root, entries))
    #input_matrix_size_btn.pack(pady=10)
def try_create_matrices_window(coherence_index_percent, analyse_frame, criteria_entries_list):
    if (less_than_ten(coherence_index_percent)):
        matrices_window = tk.Toplevel()
        matrices_window.title('matrices')

        options_label = tk.Label(matrices_window, text='Enter the number of options')
        options_label.pack(side='top')

        submit_options_btn = tk.Button(matrices_window, text='submit')
        submit_options_btn.pack(side='top')

        sub_matrix = make_matrix_based_on_given_size(len(criteria_entries_list))

        sub_entries = []
        sub_entries_list = []

        create_change_options(matrices_window, len(criteria_entries_list),
                              sub_entries_list, sub_entries)
        print(sub_entries_list)

        #matrix_frame = tk.Frame(matrices_window)
        #matrix_frame.pack(pady='10')
        #create_matrix_entry(matrix_frame, len(criteria_entries_list), sub_entries, sub_matrix)

        #submit_input_btn_sub_matrix(matrices_window, sub_matrix, sub_entries, criteria_entries_list)
    else:
        fail = tk.Label(analyse_frame, text='coherence_index_percent cannot be more than 10%', fg='red')
        fail.pack(side='left')