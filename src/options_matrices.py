from analyse_matrix_folder.extract_input import extract_criteria_input
import tkinter as tk

from making_entries.create_matrix_entry import create_matrix_entry
from making_matrices import make_matrix_based_on_given_size
from submit_input_btn_sub_matrices import submit_input_btn_sub_matrix

def on_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def make_sub_matrix_setup(matrices_frame_and_btn, options_entries, options_entries_list, criteria_entries_list, current_criteria, priority_vectors):
    criteria_label = tk.Label(matrices_frame_and_btn, text=f'{current_criteria}', font=('Helvetica', 12, 'bold'), bg='white')
    criteria_label.pack(side='top', pady=10)

    matrix_frame = tk.Frame(matrices_frame_and_btn)
    matrix_frame.pack(side='top')

    sub_matrix = make_matrix_based_on_given_size(len(options_entries))

    sub_entries = []
    create_matrix_entry(matrix_frame, len(options_entries), sub_entries, sub_matrix, options_entries_list)

    submit_input_btn_sub_matrix(matrices_frame_and_btn, sub_matrix, sub_entries, criteria_entries_list, priority_vectors)

def create_options_matrices(options_entries_list, options_entries, criteria_entries_list, priority_vectors, options_btn):
    options_btn.configure(state=tk.DISABLED)
    extract_criteria_input(options_entries_list, options_entries)

    matrices_window = tk.Toplevel()
    matrices_window.title('Matrices')
    matrices_window.geometry('800x600')

    canvas = tk.Canvas(matrices_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    vsb = tk.Scrollbar(matrices_window, command=canvas.yview, orient=tk.VERTICAL)
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=vsb.set)

    hsb = tk.Scrollbar(matrices_window, command=canvas.xview, orient=tk.HORIZONTAL)
    hsb.pack(side=tk.BOTTOM, fill=tk.X)
    canvas.configure(xscrollcommand=hsb.set)

    canvas.bind("<Configure>", lambda event: on_configure(canvas))

    frame = tk.Frame(canvas, bg='#f0f0f0')
    canvas.create_window((0, 0), window=frame, anchor="nw")

    for i, elem in enumerate(criteria_entries_list):
        current_criteria = criteria_entries_list[i]
        matrices_frame_and_btn = tk.Frame(frame, bg='#ffffff', padx=10, pady=10, borderwidth=2, relief='ridge')
        matrices_frame_and_btn.pack(side='left', padx=10, pady=10)
        make_sub_matrix_setup(matrices_frame_and_btn, options_entries, options_entries_list, criteria_entries_list, current_criteria, priority_vectors)

    submit_all_btn = tk.Button(matrices_window, text='Submit All', command=lambda: calculate_display_results(priority_vectors, options_entries_list), bg='#3498db', fg='#ffffff', font=('Helvetica', 12, 'bold'))
    submit_all_btn.pack(side='bottom', anchor='center', pady=20)

def calculate_display_results(priority_vectors, options_entries_list):
    priority_vectors = [tuple(priority_vector[:-1]) for priority_vector in priority_vectors]
    main_priority_vector = priority_vectors[0]
    options_priority_vectors = priority_vectors[1:]

    results_window = tk.Toplevel()
    results_window.title('Results')
    results_window.geometry('400x400')
    results_window.config(bg='#ecf0f1')  # Set background color
    try:
        sums = []

        for i in range(len(options_priority_vectors[0])):
            sum_ = sum(options_priority_vectors[j][i] * main_priority_vector[j] for j in range(len(main_priority_vector)))
            sums.append(sum_)
            option_result_label = tk.Label(results_window, text=f'{options_entries_list[i]}: {sum_}', font=('Helvetica', 10), bg='#ecf0f1')
            option_result_label.pack(pady=10)

        largest_num = max(sums)

        try:
            winner_index = sums.index(largest_num)
            if 0 <= winner_index < len(options_entries_list):
                winner_text = f'Winner: {options_entries_list[winner_index]} = {largest_num}'
            else:
                winner_text = 'IndexError: list index out of range'
        except ValueError:
            winner_text = 'IndexError: list index out of range'

        winner_result_label = tk.Label(results_window, text=winner_text, font=('Helvetica', 14, 'bold'), bg='#ecf0f1')
        winner_result_label.pack(pady=20)
    except (NameError, TypeError, ValueError, IndexError) as e:
        error_label = tk.Label(results_window, text=f"Not all matrices are legit", fg='red')
        error_label.pack(side='top')
