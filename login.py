import tkinter as tk
from tkinter import messagebox
import subprocess

class LoginGUI:
    def __init__(self, window):
        self.window = window
        self.window.title("Login")

        # Create GUI widgets
        self.background_image = tk.PhotoImage(file="login2.png")
        self.background_label = tk.Label(window, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.pack(fill="both", expand=True)

        self.username_label = tk.Label(window, text="Username", font=("Arial", 14), bg="#ffffff")
        self.username_label.place(relx=0.5, rely=0.4, anchor="center")
        self.username_entry = tk.Entry(window, font=("Arial", 14))
        self.username_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.password_label = tk.Label(window, text="Password", font=("Arial", 14), bg="#ffffff")
        self.password_label.place(relx=0.5, rely=0.5, anchor="center")
        self.password_entry = tk.Entry(window, show="*", font=("Arial", 14))
        self.password_entry.place(relx=0.5, rely=0.55, anchor="center")

        self.login_button = tk.Button(window, text="Login", font=("Arial", 14), bg="#4CAF50", fg="#ffffff", activebackground="#3e8e41", activeforeground="#ffffff", relief="flat", command=self.login)
        self.login_button.place(relx=0.5, rely=0.65, anchor="center")

    def login(self):
        # Check if username and password are correct
        if self.username_entry.get() == "admin" and self.password_entry.get() == "password":
            # Run another Python script if login is successful
            subprocess.Popen(["python", "main.py"])
            self.window.destroy()
        else:
            # Show error message if login is unsuccessful
            messagebox.showerror("Error", "Incorrect username or password")

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("1280x720")
    login = LoginGUI(window)
    window.mainloop()
