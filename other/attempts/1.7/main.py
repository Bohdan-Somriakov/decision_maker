import tkinter as tk
import numpy as np
from create_matrix_entry import create_matrix_entry
from create_matrix_entry import extract_input

root = tk.Tk()
root.title("root")
entries = []
def make_matrix_based_on_size(matrix_size_entry, root, entries):
    global matrix_size
    matrix_size = int(matrix_size_entry.get())
    global matrix
    matrix = np.zeros((matrix_size, matrix_size))
def main_submit(matrix_size_entry, root, entries):
    entries.clear()
    make_matrix_based_on_size(matrix_size_entry, root, entries)
    create_matrix_entry(root, matrix_size, entries, matrix)
    submit_input_btn()
def main_entry_btn_label():
    input_matrix_size_label = tk.Label(root, text='Enter the size of the matrix').pack()
    matrix_size_entry = tk.Entry(root, width=5)
    matrix_size_entry.pack()
    input_matrix_size_btn = tk.Button(root, text='submit',
                                      command=lambda: main_submit(matrix_size_entry, root, entries))
    input_matrix_size_btn.pack(pady=10)
def submit_input_btn():
    button = tk.Button(root, text='Get input', command=lambda: extract_input(entries, matrix))
    button.pack(pady=10)


main_entry_btn_label()

root.mainloop()

print("Modified Matrix outside Tkinter event loop:")
print(matrix)
