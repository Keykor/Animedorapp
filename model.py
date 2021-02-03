from datetime import timedelta, datetime
import time

class Model():
    def __init__(self):
        self.clock = Clock(1)

class Clock():
    def __init__(self, duration):
        self._duration = timedelta(minutes=duration)
        self._state = ClockStateDefault(self._duration)

    def remaining_time(self):
        if (self._state.remaining_time() <= timedelta(seconds=0)):
            self._state = ClockStateFinished()
        return self._state.remaining_time()

    def start_countdown(self):
        self._state = ClockStateStarted(self._duration)

    def reset_countdown(self):
        self._state = ClockStateDefault(self._duration)

    def has_started(self):
        return self._state.has_started()

    def has_finished(self):
        return self._state.has_finished()

class ClockStateDefault():
    def __init__(self, duration):
        self._duration = duration
        self._endTime = datetime.now() + self._duration   

    def remaining_time(self):
        return self._duration

    def has_started(self):
        return False

    def has_finished(self):
        return False

class ClockStateStarted(ClockStateDefault):
    def __init__(self, duration):
        super(ClockStateStarted, self).__init__(duration)

    def remaining_time(self):
        return self._endTime - datetime.now()

    def has_started(self):
        return True

class ClockStateFinished(ClockStateDefault):
    def __init__(self):
        super(ClockStateFinished, self).__init__(timedelta(hours=0))

    def has_started(self):
        return True

    def has_finished(self):
        return True