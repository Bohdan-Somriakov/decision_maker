from analyse_matrix_folder.extract_input import extract_criteria_input


def create_options_matrices(options_entries_list, options_entries, criteria_entries_list):
    extract_criteria_input(options_entries_list, options_entries)
    print(options_entries_list)
    print(criteria_entries_list)

    #sub_matrix = make_matrix_based_on_given_size(len(criteria_entries_list))

    # matrix_frame = tk.Frame(matrices_window)
    # matrix_frame.pack(pady='10')
    # create_matrix_entry(matrix_frame, len(criteria_entries_list), sub_entries, sub_matrix)

    # submit_input_btn_sub_matrix(matrices_window, sub_matrix, sub_entries, criteria_entries_list)