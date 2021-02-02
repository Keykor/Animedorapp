import tkinter as tk

class View():
    def __init__(self, root):
        self.root = root
        root.title("DORO")
        root.geometry("400x200")
        self.b = tk.Button(root, text='BOTONAZO')
        self.b.pack()