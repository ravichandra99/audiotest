import requests
from requests.structures import CaseInsensitiveDict
import threading
# from screenly_ose import Screenly


def switch_asset(_id):
	url = "https://00f21faea7f8b4d4c264c01882fba8dd.balena-devices.com/api/v1/assets/control/"+"asset&{}".format(_id)

	headers = CaseInsensitiveDict()
	headers["Content-Type"] = "application/json"


	resp = requests.get(url, headers=headers)

	return resp.status_code


class TestThreading(object):
    def __init__(self,_id, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=(_id,))
        thread.daemon = True
        thread.start()

    def run(self,_id):
            switch_asset(_id)


