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
        self.view.timerReset.bind("<Button>", self.reset_clock)
        self.view.timerStart.bind("<Button>", self.start_clock)

    def run(self):
        self.root.mainloop()

    def update_clock(self):
        self.view.timerLabel['text'] = self.model.clock.actual_time()

    def start_clock(self, event):
        if (not self.model.clock.has_started()):
            self.model.clock.start_countdown()
            self.countdown()

    def reset_clock(self, event):
        if (self.last_delayed_function):
            self.view.timerLabel.after_cancel(self.last_delayed_function)
            self.last_delayed_function = None
        self.model.clock.reset_countdown()
        self.update_clock()

    def countdown(self):
        if (not self.model.clock.has_finished()):
            self.model.clock.remove_one_second()
            self.update_clock()
            self.last_delayed_function = self.view.timerLabel.after(1000, self.countdown)