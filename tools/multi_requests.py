import json

from app.libs.request_helper import RequestHelper


def request_task():
    file_path = "./case_data.json"
    datas = None
    with open(file_path) as f:
        datas = json.load(f, encoding='utf-8')  # js是转换后的字典

    url = "http://192.168.11.220:5001/api/tasks"

    datas = datas[100:150]

    for data in datas:
        request_data = {
            "caseName": data["casename"],
        }
        res = RequestHelper().post(url, request_data)
        print(res.json())


def request_task_2():
    file_path = "./test.json"
    datas = None
    with open(file_path) as f:
        datas = json.load(f, encoding='utf-8')  # js是转换后的字典

    url = "http://192.168.11.220:5001/api/tasks"

    for data in datas:
        request_data = {
            "caseName": data,
        }
        res = RequestHelper().post(url, request_data)
        print(res.json())


if __name__ == "__main__":
    # request_task_2()
    request_task()
