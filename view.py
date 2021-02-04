import tkinter as tk

class View():
    def __init__(self, root):
        self.root = root
        root.title("Animedoro-app")
        root.geometry("600x200")
        root.resizable(False,False)
        root.configure(bg="#393A3A")
        self.createLeftTimer()
        self.createRightTimer()
        
    def createLeftTimer(self):
        leftFrame = tk.Frame(self.root, width=200, height=200)
        leftFrame.pack(side=tk.LEFT)
        leftFrame.pack_propagate(0)

        self.leftTimerLabel = tk.Label(leftFrame, background="black", fg="green", font=("Roboto", 20, "bold"))
        self.leftTimerStart = tk.Button(leftFrame, text="Start", background="green", fg="white", font=("Roboto", 10))
        self.leftTimerStop = tk.Button(leftFrame, text="Stop", background="red", fg="white", font=("Roboto", 10))
        self.leftTimerReset = tk.Button(leftFrame, text="Reset", background="gray", fg="white", font=("Roboto", 10))

        self.leftTimerLabel.pack(fill = tk.BOTH, expand = True)
        self.leftTimerStart.pack(fill = tk.BOTH, expand = True)
        self.leftTimerStop.pack(fill = tk.BOTH, expand = True)
        self.leftTimerReset.pack(fill = tk.BOTH, expand = True)

    def createRightTimer(self):
        rightFrame = tk.Frame(self.root, width=200, height=200)
        rightFrame.pack(side=tk.RIGHT)
        rightFrame.pack_propagate(0)

        self.rightTimerLabel = tk.Label(rightFrame, background="black", fg="green", font=("Roboto", 20, "bold"))
        self.rightTimerStart = tk.Button(rightFrame, text="Start", background="green", fg="white", font=("Roboto", 10))
        self.rightTimerStop = tk.Button(rightFrame, text="Stop", background="red", fg="white", font=("Roboto", 10))
        self.rightTimerReset = tk.Button(rightFrame, text="Reset", background="gray", fg="white", font=("Roboto", 10))

        self.rightTimerLabel.pack(fill = tk.BOTH, expand = True)
        self.rightTimerStart.pack(fill = tk.BOTH, expand = True)
        self.rightTimerStop.pack(fill = tk.BOTH, expand = True)
        self.rightTimerReset.pack(fill = tk.BOTH, expand = True)