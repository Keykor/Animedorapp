from datetime import timedelta, datetime
import time

class Model():
    def __init__(self):
        self.clock = Clock(60, "Animedoro")

    def create_new_clock(self, duration, clock_name):
        self.clock = Clock(duration, clock_name)

class Clock():
    def __init__(self, duration, clock_name):
        self._duration = timedelta(minutes=duration)
        self._clock_name = clock_name
        self._state = ClockStateDefault(self)

    def remaining_time(self):
        return self._state.remaining_time()

    def start_countdown(self):
        self._state.start_countdown()

    def reset_countdown(self):
        self._state.reset_countdown()

    def stop_countdown(self):
        self._state.stop_countdown()

    def has_finished(self):
        return self._state.has_finished()

    def on_going(self):
        return self._state.on_going()

    def state_text(self):
        return self._state.state_text()

    def change_state(self, new_state):
        self._state = new_state

    def original_duration(self):
        return self._duration

    def clock_name(self):
        return self._clock_name

class ClockStateDefault():
    def __init__(self, clock):
        self._clock = clock
        self._duration = clock.original_duration()
        self._endTime = datetime.now() + self._duration

    def remaining_time(self):
        return self._duration

    def start_countdown(self):
        self._clock.change_state(ClockStateStarted(self.remaining_time(), self._clock))

    def reset_countdown(self):
        self._clock.change_state(ClockStateDefault(self._clock))

    def stop_countdown(self):
        pass

    def has_finished(self):
        return False  

    def on_going(self):
        return False

    def state_text(self):
        return self._clock.clock_name()

class ClockStateStarted(ClockStateDefault):
    def __init__(self, duration, clock):
        super(ClockStateStarted, self).__init__(clock)
        self._duration = duration

    def start_countdown(self):
        pass

    def stop_countdown(self):
        self._clock.change_state(ClockStateStopped(self.remaining_time(), self._clock))

    def remaining_time(self):
        remaining_time = self._endTime - datetime.now()
        if (remaining_time <= timedelta(seconds=0)):
            self._clock.change_state(ClockStateFinished(self._clock))
            return timedelta(hours=0)
        return remaining_time

    def on_going(self):
        return True

    def state_text(self):
        return "On going"

class ClockStateStopped(ClockStateDefault):
    def __init__(self, duration, clock):
        super(ClockStateStopped, self).__init__(clock)
        self._duration = duration

    def start_countdown(self):
        self._clock.change_state(ClockStateStarted(self.remaining_time(), self._clock))

    def on_going(self):
        return True

    def state_text(self):
        return "Stopped"

class ClockStateFinished(ClockStateDefault):
    def __init__(self, clock):
        super(ClockStateFinished, self).__init__(clock)
        self._duration = timedelta(hours=0)

    def start_countdown(self):
        pass

    def stop_countdown(self):
        pass

    def has_finished(self):
        return True  

    def state_text(self):
        return "Finished"