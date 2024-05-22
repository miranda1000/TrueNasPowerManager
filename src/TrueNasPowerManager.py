import asyncio

class TrueNasPowerManager:
    def __init__(self, config_file: str):
        self._config_file = config_file

    async def run(self):
        while True:
            print("I'm doing things!")
            await asyncio.sleep(5) # not really

    def sync_run(self):
        """
        Same as run(), but without returning the `async` promise
        """
        asyncio.run(self.run())