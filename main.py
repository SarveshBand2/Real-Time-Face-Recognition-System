import tkinter as tk
import subprocess

class ScriptRunnerGUI:
    def __init__(self, window):
        self.window = window
        self.window.geometry("1920x1070")
        self.window.title("Home")

        # Create GUI widgets
        self.background_image = tk.PhotoImage(file="main.png")
        self.background_label = tk.Label(window, image=self.background_image)
        self.background_label.place(x=0, y=0,relheight=1)

        '''self.title_label = tk.Label(window, text="\n\n\nReal Time Face recognition System", font=("Arial", 24), fg="#ffffff", bg= "",compound='top', anchor="center")
        self.title_label.pack()'''
        
        self.button1_image = tk.PhotoImage(file="button1.png")
        self.button1 = tk.Button(window, image=self.button1_image, text="Face Data", font=("Arial", 14), compound="top", bg="white", fg="#000000", activebackground="#3e8e41", activeforeground="#ffffff", relief="flat", command=self.run_script1)
        self.button1.pack(side="left", padx=20, pady=20)

        self.button2_image = tk.PhotoImage(file="button2.png")
        self.button2 = tk.Button(window, image=self.button2_image, text="Train Dataset", font=("Arial", 14), compound="top", bg="white", fg="#000000", activebackground="#3e8e41", activeforeground="#ffffff", relief="flat", command=self.run_script2)
        self.button2.pack(side="left", padx=20, pady=20)

        self.button3_image = tk.PhotoImage(file="button3.png")
        self.button3 = tk.Button(window, image=self.button3_image, text="Face Recognition", font=("Arial", 14), compound="top", bg="white", fg="#000000", activebackground="#3e8e41", activeforeground="#ffffff", relief="flat", command=self.run_script3)
        self.button3.pack(side="left", padx=20, pady=20)

        self.quit_image = tk.PhotoImage(file="quit1.png")
        self.quit_button = tk.Button(window, image=self.quit_image, text="Quit", font=("Arial", 14), compound="top", bg="white", fg="#000000", activebackground="#3e8e41", activeforeground="#ffffff", relief="flat", command=self.quit)
        self.quit_button.pack(side="left", padx=20, pady=20)

        '''self.script1_button = tk.Button(window, text="Run Script 1", command=self.run_script1)
        self.script1_button.pack()

        self.script2_button = tk.Button(window, text="Run Script 2", command=self.run_script2)
        self.script2_button.pack()

        self.script3_button = tk.Button(window, text="Run Script 3", command=self.run_script3)
        self.script3_button.pack()

        self.quit_button = tk.Button(window, text="Quit", command=self.quit)
        self.quit_button.pack()'''

    def run_script1(self):
        subprocess.Popen(["python", "face_dataset.py"])

    def run_script2(self):
        subprocess.Popen(["python", "face_training.py"])

    def run_script3(self):
        subprocess.Popen(["python", "face_recognition.py"])

    def quit(self):
        subprocess.Popen(["python", "login.py"])
        self.window.destroy()

if __name__ == "__main__":
    window = tk.Tk()
    script_runner = ScriptRunnerGUI(window)
    window.mainloop()
