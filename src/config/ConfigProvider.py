from entities.time.TimeInterval import TimeInterval

class ConfigProvider:
    @property
    def truenas_ip(self) -> str:
        pass

    @property
    def truenas_api_key(self) -> str:
        pass

    @property
    def check_interval(self) -> TimeInterval:
        pass

    @property
    def polling_time(self) -> float:
        pass