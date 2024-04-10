import tkinter as tk
def display_sum(n, root, sums):
    sum_frame = tk.Frame(root)
    sum_frame.pack(side='top')
    label_sum = tk.Label(sum_frame, text='Sum:' + 8*' ')
    label_sum.grid(row=0, column=0)

    for i in range(n):
        label = tk.Label(sum_frame, text=f"{round(sums[i], 2):.2f}", width=8)
        label.grid(row=0, column=i + 1)


def display_eigenvector_and_priority_vector(eigenvector, priority_vector, root):
    vectors_frame = tk.Frame(root)
    eigenvector_frame = tk.Frame(vectors_frame)
    priority_vector_frame = tk.Frame(vectors_frame)
    vectors_frame.pack(side='top')
    display_eigenvector(eigenvector_frame, eigenvector, root)
    display_priority_vector(priority_vector_frame, priority_vector, root)


def display_eigenvector(eigenvector_frame, eigenvector, root):
    eigenvector_frame.pack(side='left')
    eigenvector_label = tk.Label(eigenvector_frame, text='eigenvector', width=10)
    eigenvector_label.grid(row=0, column=0)
    for i in range(len(eigenvector)):
        label_eigenvector_elem = tk.Label(eigenvector_frame, text=f'{round(eigenvector[i], 2):.2f}', width=8)

        label_eigenvector_elem.grid(row=i+1, column=0)


def display_priority_vector(priority_vector_frame, priority_vector, root):
    priority_vector_frame.pack(side='left')
    eigenvector_label = tk.Label(priority_vector_frame, text='priority vector', width=10)
    eigenvector_label.grid(row=0, column=0)
    for i in range(len(priority_vector)):
        label_eigenvector_elem = tk.Label(priority_vector_frame, text=f'{round(priority_vector[i], 2):.2f}', width=8)

        label_eigenvector_elem.grid(row=i + 1, column=0)


def display_lambda_max(lambda_max, root):
    lambda_max_frame = tk.Frame(root)
    lambda_max_frame.pack(side='top')
    label_lambda_max = tk.Label(lambda_max_frame, text='lambda_max:', pady=10)
    label_lambda_max.grid(row=0, column=0)
    for i in range(len(lambda_max)):
        label_lambda_max = tk.Label(lambda_max_frame, text=f'{round(lambda_max[i], 2):.2f}', width=8)
        label_lambda_max.grid(row=0, column=i+1)


def display_coherence_index_percent(coherence_index_percent, root):
    display_variable('coherence_index_percent', coherence_index_percent, root)


def display_coherence_index(coherence_index, root):
    display_variable('coherence_index', coherence_index, root)


def display_lambda_max_sum(lambda_max_sum, root):
    display_variable('lambda_max_sum', lambda_max_sum, root)


def display_variable(frame_title, variable_value, root):
    variable_frame = tk.Frame(root)
    variable_frame.pack(side='top')

    title_label = tk.Label(variable_frame, text=f'{frame_title}:')
    title_label.grid(row=0, column=1)

    value_label = tk.Label(variable_frame, text=f'{round(variable_value, 2):.2f}')
    value_label.grid(row=0, column=2)
