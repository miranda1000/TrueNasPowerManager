from .Clock import Clock
from .ClockFactory import ClockFactory
from .SystemClock import SystemClock

class SystemClockFactory(ClockFactory):
    def create(self) -> Clock:
        return SystemClock()