import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Disappearing Text App")
text_widget = tk.Text(window, height=10, width=50, font=("Gill Sans", 14))
text_widget.pack(pady=20)
countdown_time = 3000
timer = None


def start_timer():
    global timer
    if timer:
        window.after_cancel(timer)
    timer = window.after(countdown_time, clear_text)


def reset_timer(event=None):
    start_timer()


def clear_text():
    text = text_widget.get(1.0, tk.END).strip()  # .strip() is to remove leading and trailing white space
    if text:
        text_widget.delete(1.0, tk.END)
        messagebox.showinfo("Time's up!", "You stopped typing. Your work has been cleared!")


text_widget.bind("<KeyPress>", reset_timer)


if __name__ == "__main__":
    window.mainloop()
