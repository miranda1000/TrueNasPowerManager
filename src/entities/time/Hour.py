from __future__ import annotations

class Hour:
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def minute(self) -> int:
        return self._minute

    @property
    def second(self) -> int:
        return self._second

    def __repr__(self) -> str:
        return f"Hour({self._hour:02}:{self._minute:02}:{self._second:02})"

    def __lt__(self, other: Hour) -> bool:
        if self._hour < other._hour:
            return True
        elif self._hour == other._hour:
            if self._minute < other._minute:
                return True
            elif self._minute == other._minute:
                if self._second < other._second:
                    return True
                    
        return False # equal or greater

    def __eq__(self, other: Hour) -> bool:
        return self._hour == other._hour and self._minute == other._minute and self._second == other._second

    def __hash__(self) -> hash:
        return hash((self._hour, self._minute, self._second))

    def __gt__(self, other: Hour) -> bool:
        return (not (self < other)) and (not (self == other))

    def __le__(self, other: Hour) -> bool:
        return (self < other) or (self == other)

    def __ge__(self, other: Hour) -> bool:
        return (self > other) or (self == other)
        
    def __ne__(self, other: Hour) -> bool:
        return not (self == other)