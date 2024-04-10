import tkinter as tk
import numpy as np
from create_matrix_entry import create_entry_widget
from create_matrix_entry import create_lables_column
from create_matrix_entry import create_labels_row
from create_matrix_entry import get_input

root = tk.Tk()
root.title("root")

matrix_size = 3
def input_matrix_size(matrix_size_entry):
    matrix_size = matrix_size_entry.get()
    print(matrix_size)


#matrix_size = 3
input_matrix_size_label = tk.Label(root, text='Enter the size of the matrix').pack()
matrix_size_entry = tk.Entry(root, width=5)
matrix_size_entry.pack()
input_matrix_size_btn = tk.Button(root, text='submit', command=lambda: input_matrix_size(matrix_size_entry))
input_matrix_size_btn.pack(pady=10)
entries = []

matrix = np.zeros((matrix_size, matrix_size))

matrix_frame = tk.Frame(root)
matrix_frame.pack(side="top")

create_labels_row(matrix_size, matrix_frame)
create_lables_column(matrix_size, matrix_frame)
create_entry_widget(matrix_size, matrix_frame, entries)
get_input(entries, matrix)

button = tk.Button(root, text='Get input', command=lambda: get_input(entries, matrix))
button.pack(pady=10)


root.mainloop()

print("Modified Matrix outside Tkinter event loop:")
print(matrix)
