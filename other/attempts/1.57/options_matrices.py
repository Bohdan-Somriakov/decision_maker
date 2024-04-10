from analyse_matrix_folder.extract_input import extract_criteria_input
import tkinter as tk

from making_entries.create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix

def on_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def make_sub_matrix_setup(matrices_frame_and_btn, options_entries, options_entries_list, criteria_entries_list, current_criteria, priority_vectors):
    criteria_label = tk.Label(matrices_frame_and_btn, text=f'{current_criteria}')
    criteria_label.pack(side='top')

    matrix_frame = tk.Frame(matrices_frame_and_btn)
    matrix_frame.pack(side='top')

    sub_matrix = make_matrix_based_on_given_size(len(options_entries))

    sub_entries = []
    create_matrix_entry(matrix_frame, len(options_entries), sub_entries, sub_matrix, options_entries_list)

    submit_input_btn_sub_matrix(matrices_frame_and_btn, sub_matrix, sub_entries, criteria_entries_list, priority_vectors)

def create_options_matrices(options_entries_list, options_entries, criteria_entries_list, priority_vectors):

    extract_criteria_input(options_entries_list, options_entries)

    matrices_window = tk.Toplevel()
    matrices_window.title('matrices')

    canvas = tk.Canvas(matrices_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    vsb = tk.Scrollbar(matrices_window, command=canvas.yview, orient=tk.VERTICAL)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=vsb.set)

    hsb = tk.Scrollbar(matrices_window, command=canvas.xview, orient=tk.HORIZONTAL)
    hsb.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.configure(xscrollcommand=hsb.set)

    canvas.bind("<Configure>", lambda event: on_configure(canvas))

    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    print(criteria_entries_list)

    for i, elem in enumerate(criteria_entries_list):
        current_criteria = criteria_entries_list[i]
        matrices_frame_and_btn = tk.Frame(frame)
        matrices_frame_and_btn.pack(side='left')
        make_sub_matrix_setup(matrices_frame_and_btn, options_entries, options_entries_list, criteria_entries_list, current_criteria, priority_vectors)

    submit_all_btn = tk.Button(matrices_window, text='submit all',
                               command=lambda: calculate_display_results(priority_vectors,  options_entries_list))
    submit_all_btn.pack(side='bottom', anchor='center')
def calculate_display_results(priority_vectors, options_entries_list):
    priority_vectors = [tuple(priority_vector[:-1]) for priority_vector in priority_vectors]
    main_priority_vector = priority_vectors[0]
    options_priority_vectors = priority_vectors[1:]

    answer_list = list()

    for i in range(options_priority_vectors):
        answer_list.append(sum(option[i] * weight for option, weight in zip(options_priority_vectors, main_priority_vector)))
    print(options_priority_vectors)
