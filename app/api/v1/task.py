from app.celery_task.celery_app import celery
from app.config import TASK_CASE_FILEPATH
from app.libs.error_code import ServerError, Success
from app.libs.redprint import Redprint
from flask import request
from app.celery_task.detect_task import detect_task
from app.libs.response import ResultResponse
from app.libs.file_helper import FileHelper

api = Redprint('tasks')


@api.route('', methods=['POST'])
def create_task():
    """创建任务

    @@@
    #### body参数

    | args | nullable | type | remark |
    |--------|--------|--------|--------|
    |    caseName    |    false    |    string   |    案例名字    |
    #### return
    - ##### json
    > {
        "error_code": 0,
        "msg": "ok",
        "request": "GET /api/tasks"
        "data": {"task_id": "f33f192c-2658-44c4-a049-0ae5794edd61"}
      }

    #### example
    ```
    url='http://127.0.0.1:5001/api/tasks'
    ```
    @@@
    """
    resp = ResultResponse()

    # i = celery.control.inspect()
    # print(i.active())

    task_id = ""
    force = None
    data = {}

    datas = []

    param_dict = request.json
    if 'force' in param_dict.keys():
        force = request.json['force']

    case_name = request.json['caseName']

    file_path = TASK_CASE_FILEPATH

    datas = FileHelper.get_json_data(file_path)
    for d in datas:
        if d["case_name"] == case_name:
            task_id = d["task_id"]
            break

    if force == "True" or force == 1 or task_id == "":
        task = detect_task.apply_async(args=[case_name])
        data["task_id"] = task.id

        data_task_case = {
            "task_id": task.id,
            "case_name": case_name,
        }

        isContain = False

        for d in datas:
            if d["case_name"] == case_name:
                d["task_id"] = task.id
                isContain = True
                break

        if isContain is False:
            datas.append(data_task_case)
        FileHelper.save_json_data(file_path, datas)
    elif task_id != "":
        data["task_id"] = task_id

    resp.data = data
    return resp


@api.route('/<task_id>/result', methods=['GET'])
def task_result(task_id):
    resp = ResultResponse()

    task = detect_task.AsyncResult(task_id)

    print(task.ready())
    print("state ===", task.state)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }

        resp.data = response
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']

        resp.data = response
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }

        resp.data = response

    return resp


@api.route('/<task_id>/progress', methods=['POST'])
def update_task_progress(task_id):
    progress = request.json['progress']
    detect_task.update_state(task_id=task_id,
                             state='PROGRESS',
                             meta={'current': progress, 'total': 100,
                                   'status': ""})

    return Success()
