from __future__ import annotations
import requests
import urllib3

class TrueNasApi:
    def __init__(self, ip: str, token: str):
        self._ip = ip
        self.__token = token

    def connect(self):
        print("[i] Connecting to TrueNAS...")

        # We don't have to do anything to connect.
        # However, to detect if the instance is running
        # we'll execute something
        try:
            self.get_pending_jobs() # discard return
        except Exception:
            # something wrong happened
            raise requests.Timeout(f"Couldn't connect to TrueNAS on {self._ip}")

        print("[i] Connected to TrueNAS.")

    def close(self):
        print("[i] Closing TrueNAS connection...")
        # we don't have to do anything

    def __get(self, endpoint: str) -> dict:
        url = f"http://{self._ip}/api/v2.0{endpoint}"
        headers = {"Authorization": "Bearer " + self.__token}

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # stops the "InsecureRequestWarning" messagess
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code != 200:
            raise Exception(f"Couldn't make get request: error {response.status_code}\nWeb contents: {response.text}")
        
        return response.json()

    def __post(self, endpoint: str, data: dict = {}):
        url = f"http://{self._ip}/api/v2.0{endpoint}"
        headers = {"Authorization": "Bearer " + self.__token}

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) # stops the "InsecureRequestWarning" messagess
        response = requests.post(url, data=data, headers=headers, verify=False)
        if response.status_code != 200:
            raise Exception(f"Couldn't make get request: error {response.status_code}\nWeb contents: {response.text}")

    def get_pending_jobs(self) -> dict:
        jobs = self.__get('/core/get_jobs')
        return [ job for job in jobs if job['state'] == 'RUNNING' ]

    @property
    def processing_jobs(self) -> bool:
        jobs = self.get_pending_jobs()
        return len(jobs) > 0

    def shutdown(self):
        self.__post('/system/shutdown')


    def __enter__(self) -> TrueNasApi:
        self.connect()
        return self

    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.close()