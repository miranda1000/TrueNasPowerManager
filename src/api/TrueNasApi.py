import requests

class TrueNasApi:
    def __init__(self, ip: str, token: str):
        self._ip = ip
        self.__token = token

    def connect(self):
        pass # not needed

    def __get(self, endpoint: str) -> dict:
        url = f"http://{self._ip}//api/v2.0/{endpoint}"
        headers = {"Authorization": "Bearer " + self.__token}

        response = requests.get(url, headers=headers, verify=False)
        if response.status_code != 200:
            raise Exception(f"Couldn't make get request: error {response.status_code}\nWeb contents: {response.text}")
        
        return response.json()

    def __post(self, endpoint: str, data: dict = {}):
        url = f"http://{self._ip}//api/v2.0/{endpoint}"
        headers = {"Authorization": "Bearer " + self.__token}

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