from typing import Union
from .Hour import Hour
from .HourFactory import HourFactory

class TimeInterval:
    def __init__(self, start: Union[str,Hour], end: Union[str,Hour]):
        # convert to date (if needed)
        if isinstance(start, str):
            start = HourFactory.parse_hour(start)
        if isinstance(end, str):
            end = HourFactory.parse_hour(end)

        # start should be the first
        if start > end:
            start,end = end,start

        self._start = start
        self._end = end

    @property
    def start(self) -> Hour:
        return self._start

    @property
    def end(self) -> Hour:
        return self._end

    def is_within(self, time: Union[str,Hour]) -> bool:
        # convert to date (if needed)
        if isinstance(time, str):
            time = HourFactory.parse_hour(time)

        return time >= self._start and time <= self._end

    def __repr__(self) -> str:
        return f"TimeInterval({self._start},{self._end})"