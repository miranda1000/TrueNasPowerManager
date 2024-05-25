import json
import logging
from typing import Dict,Any
from os import path
from pathlib import Path


from .ConfigProvider import ConfigProvider
from entities.time.TimeInterval import TimeInterval

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
            },
            'check_interval': {
                'start': '01:00:00',
                'end': '08:00:00'
            },
            'polling_time': 120
        }

    def create(self):
        # create any parent folder needed
        Path(self._configPath).parent.mkdir(parents=True, exist_ok=True)

        # as we have nothing set, load the defaults
        self._data = JsonConfig._get_defaults()

        # create the file
        with open(self._configPath, 'w') as f:
            json.dump(self._data, f, indent=2)

    def read(self, create_if_not_exists = True):
        if create_if_not_exists and not path.exists(self._configPath):
            logging.warning("Couldn't find config file; creating it...")
            self.create()
            return # `create` already loads the data

        with open(self._configPath, 'r') as f:
            self._data = json.load(f)

    @property
    def truenas_ip(self) -> str:
        if self._data is None:
            raise Exception("You have to call `read` first")
        return self._data['truenas']['ip']

    @property
    def truenas_api_key(self) -> str:
        if self._data is None:
            raise Exception("You have to call `read` first")
        return self._data['truenas']['api_key']

    @property
    def check_interval(self) -> TimeInterval:
        if self._data is None:
            raise Exception("You have to call `read` first")
        start = self._data['check_interval']['start']
        end = self._data['check_interval']['start']

        return TimeInterval(start,end)

    @property
    def polling_time(self) -> float:
        if self._data is None:
            raise Exception("You have to call `read` first")
        return float(self._data['polling_time'])