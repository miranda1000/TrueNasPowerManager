import json
import logging
from typing import Dict,Any
from ..entities.time.TimeInterval import TimeInterval

class JsonConfig(ConfigProvider):
    def __init__(self, path: str):
        self._configPath = path
        self._data = None

    @staticmethod
    def _get_defaults() -> Dict[str, Any]:
        return {
            'truenas': {
                'ip': '127.0.0.1',
                'api_key': ''
            }
            'check_interval': {
                'start': '01:00:00',
                'end': '08:00:00'
            }
        }

    def create(self):
        with open(self._configPath, 'w') as f:
            json.dump(JsonConfig._get_defaults(), f, indent=2)

    def read(self, create_if_not_exists = True):
        if create_if_not_exists and not os.path.exists(self._configPath):
            logging.warning("Couldn't find config file; creating it...")
            self.create()

        with open(self._configPath, 'r') as f:
            self._data = json.load(f)

    @property
    def truenas_ip(self) -> str:
        return self._data['truenas']['ip']

    @property
    def truenas_api_key(self) -> str:
        return self._data['truenas']['api_key']

    @property
    def check_interval(self) -> TimeInterval:
        start = self._data['check_interval']['start']
        end = self._data['check_interval']['start']

        return TimeInterval(start,end)