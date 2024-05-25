import asyncio
from sys import exit

from config.JsonConfig import JsonConfig
from api.TrueNasApi import TrueNasApi
from api.TrueNasApiFactory import TrueNasApiFactory
from clock.Clock import Clock
from clock.ClockFactory import ClockFactory
from clock.SystemClockFactory import SystemClockFactory

class TrueNasPowerManager:
    def __init__(self, config_file_path: str, api_endpoint_factory: TrueNasApiFactory = None, clock_factory: ClockFactory = SystemClockFactory()):
        self._config_file_path = config_file_path
        self._config_file = None

        self._clock = clock_factory.create()

        if api_endpoint_factory is None:
            api_endpoint_factory = lambda ip,token: TrueNasApi(ip,token)
        self._api_endpoint_factory = api_endpoint_factory

    async def run(self):
        self._setup()

        if not self._config_file.truenas_api_key:
            print("[w] You have to set the TrueNAS API key. Check the config file and launch the program again.")
            exit(1)

        while True:
            self._tick()

            await asyncio.sleep(self._config_file.polling_time)

    def sync_run(self):
        """
        Same as run(), but without returning the `async` promise
        """
        asyncio.run(self.run())

    def _setup(self):
        print("[i] Loading config file...")
        print(f"[v] Config file at '{self._config_file_path}'.")
        self._config_file = JsonConfig(self._config_file_path)
        self._config_file.read()

    def _tick(self) -> bool:
        # is within hours?
        now = self._clock.get_current_hour()
        print(f"[v] Current hour: {now}. (Checking against interval: {self._config_file.check_interval})")
        if not self._config_file.check_interval.is_within(now):
            # TODO instead of polling, calculate how many seconds are left until the range starts
            difference = self._config_file.polling_time
            print(f"[i] Outside check range; trying it in {difference} seconds...")
            return True

        # run the checks
        try:
            with self.__get_machine() as machine:
                processing_jobs = machine.processing_jobs # is there any scheduled job?
                print(f"[v] Got processing jobs: {processing_jobs}")

                if not processing_jobs:
                    print(f"[i] No tasks running. Shutting down...")
                    machine.shutdown() # stop the machine
            
            return True # all ok

        except Exception as ex:
            print("[e] Got an exception while trying to run commands, is the server down? Will try again later.")
            print("[e] " + str(ex))

            return False # exception

    def __get_machine(self) -> TrueNasApi:
        instance = self._api_endpoint_factory(self._config_file.truenas_ip, self._config_file.truenas_api_key)
        instance.connect()
        return instance