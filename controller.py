import tkinter as tk
from model import Model
from view import View
from datetime import timedelta

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.update_clock()
        self.view.leftTimerReset.bind("<Button>", self.reset_clock)
        self.view.leftTimerStart.bind("<Button>", self.start_clock)

    def run(self):
        self.root.mainloop()

    def update_clock(self):
        self.view.leftTimerLabel['text'] = str(self.model.clock.remaining_time()).split(".")[0]

    def start_clock(self, event):
        if (not self.model.clock.has_started()):
            self.model.clock.start_countdown()
            self.countdown()

    def reset_clock(self, event):
        self.model.clock.reset_countdown()
        self.update_clock()

    def countdown(self):
        self.update_clock()
        if (self.model.clock.has_started() and not self.model.clock.has_finished()):
            self.last_delayed_function = self.view.leftTimerLabel.after(200, self.countdown)