import tkinter as tk
from main_matrix_setup import main_entry_btn_label

def main():
    root = tk.Tk()
    root.title("root")

    main_entry_btn_label(root)
    root.configure(bg="#3498db")

    root.mainloop()

if __name__ == "__main__":
    main()


