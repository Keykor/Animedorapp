import tkinter as tk

class View():
    def __init__(self, root):
        self.root = root
        root.title("Animedoro")
        root.geometry("250x300")
        root.resizable(False,False)

        top_frame = tk.Frame(root, width=250, height=100, background="#f7f7f7")
        top_frame.pack()
        top_frame.pack_propagate(0)

        title_label = tk.Label(top_frame, background="#0275d8", fg="#f7f7f7", text="Animedoro", font=("Roboto", 25, "bold"))
        title_label.pack(side=tk.TOP, fill = tk.BOTH, expand = True)

        self.work_button = tk.Button(top_frame, text="Work", background="#5bc0de", fg="#f7f7f7", font=("Roboto", 10, "bold"))
        self.rest_button = tk.Button(top_frame, text="Rest", background="#5bc0de", fg="#f7f7f7", font=("Roboto", 10, "bold"))
        self.options_button = tk.Button(top_frame, text="Options", background="#5bc0de", fg="#f7f7f7", font=("Roboto", 10, "bold"))
        
        self.work_button.pack(side=tk.LEFT, fill = tk.BOTH, expand = True)
        self.rest_button.pack(side=tk.LEFT, fill = tk.BOTH, expand = True)
        self.options_button.pack(side=tk.LEFT, fill = tk.BOTH, expand = True)

        self.create_timer()
        
    def create_timer(self):
        timer_frame = tk.Frame(self.root, width=250, height=200, background="#f7f7f7")
        timer_frame.pack(side=tk.BOTTOM)
        timer_frame.pack_propagate(0)

        self.timer_label = tk.Label(timer_frame, background="#292b2c", fg="#5cb85c", font=("Roboto", 20, "bold"))
        self.timer_start = tk.Button(timer_frame, text="Start", background="#5cb85c", fg="#f7f7f7", font=("Roboto", 10, "bold"))
        self.timer_stop = tk.Button(timer_frame, text="Stop", background="#d9534f", fg="#f7f7f7", font=("Roboto", 10, "bold"))
        self.timer_reset = tk.Button(timer_frame, text="Reset", background="#f0ad4e", fg="#f7f7f7", font=("Roboto", 10, "bold"))

        self.timer_label.pack(fill = tk.BOTH, expand = True)
        self.timer_start.pack(fill = tk.BOTH, expand = True)
        self.timer_stop.pack(fill = tk.BOTH, expand = True)
        self.timer_reset.pack(fill = tk.BOTH, expand = True)