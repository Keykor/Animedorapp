import tkinter as tk

class View():
    def __init__(self, root):
        self.root = root
        root.title("Animedoro-app")
        root.geometry("400x200")

        self.timerLabel = tk.Label()
        self.timerStart = tk.Button(text="Start")
        self.timerReset = tk.Button(text="Reset")

        self.timerLabel.grid(column=0, row=1)
        self.timerStart.grid(column=0, row=2)
        self.timerReset.grid(column=0, row=3)