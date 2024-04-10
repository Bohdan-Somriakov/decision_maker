import tkinter as tk
import numpy as np
from create_matrix_entry import create_entry_widget
from create_matrix_entry import create_lables_column
from create_matrix_entry import create_labels_row
from create_matrix_entry import get_input



entries_size = 3
entries = []

matrix = np.zeros((entries_size, entries_size))

root = tk.Tk()
root.title("Input Field Example")

matrix_frame = tk.Frame(root)
matrix_frame.pack(side="top")

create_labels_row(entries_size, matrix_frame)
create_lables_column(entries_size, matrix_frame)
create_entry_widget(entries_size, matrix_frame, entries)
get_input(entries, matrix)

button = tk.Button(root, text='Get input', command=lambda: get_input(entries, matrix))
button.pack(pady=10)

root.mainloop()

print("Modified Matrix outside Tkinter event loop:")
print(matrix)
