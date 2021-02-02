import tkinter as tk
from model import Model
from view import View

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.view.b.bind("<Button>",self.action)

    def run(self):
        self.root.mainloop()

    def action(self, event):
        self.model.saludis()