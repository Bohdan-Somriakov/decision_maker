import tkinter as tk
import numpy as np
from create_matrix_entry import create_entry_widget
from create_matrix_entry import create_lables_column
from create_matrix_entry import create_labels_row
from create_matrix_entry import create_matrix_entry
from create_matrix_entry import get_input

root = tk.Tk()
root.title("root")

def make_matrix_based_on_size(matrix_size_entry, root, entries):
    global matrix_size
    matrix_size = int(matrix_size_entry.get())
    global matrix
    matrix = np.zeros((matrix_size, matrix_size))
def start(matrix_size_entry, root, entries):
    make_matrix_based_on_size(matrix_size_entry, root, entries)
    create_matrix_entry(root, matrix_size, entries, matrix)




#matrix_size = 3
input_matrix_size_label = tk.Label(root, text='Enter the size of the matrix').pack()
matrix_size_entry = tk.Entry(root, width=5)
matrix_size_entry.pack()
input_matrix_size_btn = tk.Button(root, text='submit', command=lambda: start(matrix_size_entry, root, entries))
input_matrix_size_btn.pack(pady=10)
entries = []


button = tk.Button(root, text='Get input', command=lambda: get_input(entries, matrix))
button.pack(pady=10)


root.mainloop()

print("Modified Matrix outside Tkinter event loop:")
print(matrix)
