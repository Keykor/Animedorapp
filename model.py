from datetime import timedelta
import time

class Model():
    def __init__(self):
        self.clock = Clock()

class Clock():
        def __init__(self):
            self._timerValue = timedelta(seconds=10)
            self._started = False
            self._finished = False

        def actual_time(self):
            return self._timerValue

        def start_countdown(self):
            self._started = True
            self._finished = False

        def reset_countdown(self):
            self._started = False
            self._finished = True
            self._timerValue = timedelta(seconds=10)

        def remove_one_second(self):
            self._timerValue = self._timerValue - timedelta(seconds=1)
            if self._timerValue == timedelta(seconds=0):
                self._finished = True

        def has_started(self):
            return self._started

        def has_finished(self):
            return self._finished