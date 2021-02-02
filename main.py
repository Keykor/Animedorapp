import tkinter as tk

class Model():
    def __init__(self):
        pass

    def saludis(self):
        print("Wenas creaturas")

class View():
    def __init__(self, master):
        self.master = master
        master.title("DORO")
        master.geometry("400x200")
        self.b = tk.Button(master, text='BOTONAZO')
        self.b.pack()

class Controller():
    def __init__(self, root):
        self.model = Model()
        self.view = View(root)
        self.view.b.bind("<Button>",self.action)

    def action(self, event):
        self.model.saludis()

if __name__ == '__main__':
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()