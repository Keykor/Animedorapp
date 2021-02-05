import tkinter as tk
import pygame
from model import Model
from view import View
from datetime import timedelta

class Controller():
    def __init__(self):
        self.root = tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self._title_message = "Animedoro"

        self.update_clock()
        self.view.timer_reset.bind("<Button>", self.reset_clock)
        self.view.timer_start.bind("<Button>", self.start_clock)
        self.view.timer_stop.bind("<Button>", self.stop_clock)
        self.view.animedoro_button.bind("<Button>", self.create_animedoro_clock)
        self.view.break_button.bind("<Button>", self.create_break_clock)

        pygame.mixer.init()
        self.finish_sound_played = False

    def run(self):
        self.root.mainloop()

    def update_clock(self):
        self.view.timer_label['text'] = str(self.model.clock.remaining_time()).split(".")[0]
        self.view.title_label['text'] = self.model.clock.state_text()
        if (self.model.clock.has_finished() and not self.finish_sound_played):
            self.finish_sound_played = True
            pygame.mixer.music.load("sound.mp3")
            pygame.mixer.music.play()

    def start_clock(self, event):
        self.model.clock.start_countdown()
        self.countdown()

    def reset_clock(self, event):
        self.model.clock.reset_countdown()
        self.update_clock()

    def stop_clock(self, event):
        self.model.clock.stop_countdown()
        self.update_clock()

    def countdown(self):
        self.update_clock()
        if (self.model.clock.on_going()):
            self.last_delayed_function = self.view.timer_label.after(200, self.countdown)

    def create_animedoro_clock(self, event):
        self.finish_sound_played = False
        self.model.create_new_clock(60, "Animedoro")
        self.update_clock()

    def create_break_clock(self, event):
        self.finish_sound_played = False
        self.model.create_new_clock(20, "Break")
        self.update_clock()