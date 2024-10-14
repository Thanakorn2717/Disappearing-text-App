import tkinter as tk
from tkinter import messagebox


class DisappearingTextApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Disappearing Text App")
        self.text_widget = tk.Text(window, height=10, width=50, font=("Gill Sans", 15))
        self.text_widget.pack(pady=20)

        self.text_widget.bind("<KeyPress>", self.reset_timer)
        self.timer = None
        self.timeout_duration = 3000  # 3000 milliseconds = 3 seconds

        self.start_timer()

    def start_timer(self):
        if self.timer:
            self.window.after_cancel(self.timer)
        self.timer = self.window.after(self.timeout_duration, self.clear_text)

    def reset_timer(self, event=None):
        self.start_timer()

    def clear_text(self):
        current_text = self.text_widget.get(1.0, tk.END).strip()
        print(current_text)
        if current_text:
            self.text_widget.delete(1.0, tk.END)
            messagebox.showinfo("Time's up!", "You stopped typing. Your work has been cleared!")


if __name__ == "__main__":
    window = tk.Tk()
    app = DisappearingTextApp(window)
    window.mainloop()
