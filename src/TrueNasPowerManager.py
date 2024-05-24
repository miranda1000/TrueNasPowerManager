import asyncio
from sys import exit

from config.JsonConfig import JsonConfig
from api.TrueNasApi import TrueNasApi
from api.TrueNasApiFactory import TrueNasApiFactory

class TrueNasPowerManager:
    def __init__(self, config_file_path: str, api_endpoint_builder: TrueNasApiFactory = None):
        self._config_file_path = config_file_path
        self._config_file = None

        if api_endpoint_builder is None:
            api_endpoint_builder = lambda ip,token: TrueNasApi(ip,token)
        self._api_endpoint_builder = api_endpoint_builder

    async def run(self):
        print("[i] Loading config file...")
        print(f"[v] Config file at '{self._config_file_path}'.")
        self._config_file = JsonConfig(self._config_file_path)
        self._config_file.read()

        if not self._config_file.truenas_api_key:
            print("[w] You have to set the TrueNAS API key. Check the config file and launch the program again.")
            exit(1)

        print("[i] Connecting to TrueNAS...")
        self.__machine = self.__get_machine()
        print("[i] Connected to TrueNAS.")

        while True:
            processing_jobs = self.__machine.processing_jobs

            # TODO temporal
            #await asyncio.sleep(5)

            #self.__machine.shutdown() # stop the machine
            break

    def sync_run(self):
        """
        Same as run(), but without returning the `async` promise
        """
        asyncio.run(self.run())

    def __get_machine(self) -> TrueNasApi:
        instance = self._api_endpoint_builder(self._config_file.truenas_ip, self._config_file.truenas_api_key)
        instance.connect()
        return instance