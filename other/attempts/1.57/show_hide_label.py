def hide_label(label):
    label.pack_forget()

def show_label(message_label):
    message_label.pack()
    # Schedule the hide_label function to be called after 3000 milliseconds (3 seconds)
    message_label.after(3000, lambda: hide_label(message_label))