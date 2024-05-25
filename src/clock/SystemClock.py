from datetime import datetime

from .Clock import Clock
from entities.time.Hour import Hour

class SystemClock(Clock):
    def get_current_hour(self) -> Hour:
        now = datetime.now()
        return Hour(hour=now.hour, minute=now.minute, second=now.second)