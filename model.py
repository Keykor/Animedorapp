from datetime import timedelta, datetime
import time

class Model():
    def __init__(self):
        self.clock = Clock(60, "Animedoro")

    def create_new_clock(self, duration, default_message):
        self.clock = Clock(duration, default_message)

class Clock():
    def __init__(self, duration, default_message):
        self._duration = timedelta(minutes=duration)
        self._state = ClockStateDefault(self._duration, default_message)
        self._default_message = default_message

    def remaining_time(self):
        if (self._state.remaining_time() <= timedelta(seconds=0)):
            self._state = ClockStateFinished()
        return self._state.remaining_time()

    def start_countdown(self):
        if (not self.has_finished()):
            self._state = ClockStateStarted(self.remaining_time())

    def reset_countdown(self):
        self._state = ClockStateDefault(self._duration, self._default_message)

    def stop_countdown(self):
        if (not self.has_finished()):
            self._state = ClockStateStopped(self.remaining_time())

    def on_going(self):
        return self.has_started() and (not self.has_stopped()) and (not self.has_finished())

    def has_started(self):
        return self._state.has_started()

    def has_finished(self):
        return self._state.has_finished()

    def has_stopped(self):
        return self._state.has_stopped()

    def state_text(self):
        return self._state.state_text()

class ClockStateDefault():
    def __init__(self, duration, message="Default"):
        self._duration = duration
        self._endTime = datetime.now() + self._duration
        self._message = message

    def remaining_time(self):
        return self._duration

    def has_started(self):
        return False

    def has_finished(self):
        return False

    def has_stopped(self):
        return False

    def state_text(self):
        return self._message

class ClockStateStarted(ClockStateDefault):
    def __init__(self, duration, message="On going"):
        super(ClockStateStarted, self).__init__(duration, message)

    def remaining_time(self):
        return self._endTime - datetime.now()

    def has_started(self):
        return True

class ClockStateStopped(ClockStateDefault):
    def __init__(self, duration, message="Stopped"):
        super(ClockStateStopped, self).__init__(duration, message)

    def has_started(self):
        return True

    def has_stopped(self):
        return True

class ClockStateFinished(ClockStateStopped):
    def __init__(self, message="Finished"):
        super(ClockStateFinished, self).__init__(timedelta(hours=0), message)

    def has_finished(self):
        return True