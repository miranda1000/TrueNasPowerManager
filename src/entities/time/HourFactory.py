from .Hour import Hour

class HourFactory:
    @staticmethod
    def parse_hour(text: str) -> Hour:
        segments = text.split(":")
        return Hour(int(segments[0]), int(segments[1]), int(segments[2]))