import json
import requests

from app.config import TASK_TIMEOUT


class RequestHelper:
    def post(self, api, data):
        headers = {"Content-Type": "application/json"}

        json_data = json.dumps(data).encode('utf-8')
        print("TASK_TIMEOUT=", TASK_TIMEOUT)
        try:
            res = requests.post(api, json=data, timeout=TASK_TIMEOUT)
            print(res.content)
            return res
        except Exception as e:
            print("exception=", str(e))
            raise Exception(str(e))
