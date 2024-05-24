from .TrueNasApi import TrueNasApi

class TrueNasApiFactory:
    def create(self, ip: str, token: str) -> TrueNasApi:
        pass