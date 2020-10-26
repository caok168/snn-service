from app.celery_task.celery_app import celery
from app.config import DETECT_API_URL, TASK_CASE_FILEPATH
from app.libs.error_code import ServiceError
from app.libs.file_helper import FileHelper
from app.libs.request_helper import RequestHelper


@celery.task(bind=True)
def detect_task(self, case_name):
    print(case_name)

    # mhd_file = "data/1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860.mhd"
    # seg_file = "seg-lungs-LUNA16/1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860.mhd"

    mhd_file = "data/{}.mhd".format(case_name)
    seg_file = "seg-lungs-LUNA16/{}.mhd".format(case_name)

    url = DETECT_API_URL
    print("detect api: {}".format(url))
    callback = "/api/tasks/{task_id}/progress".format(task_id=self.request.id)
    print("callback: {}".format(callback))

    data = {
        "mhd_file": mhd_file,
        "seg_file": seg_file,
        "callback": callback,
    }

    print("data:{}".format(data))

    resp = None

    try:
        resp = RequestHelper().post(url, data)
        resp.raise_for_status()
    except Exception as e:
        self.update_state(task_id=self.request.id,
                          state='FAILURE',
                          )

        datas = FileHelper.get_json_data(TASK_CASE_FILEPATH)
        for data in datas:
            if data["case_name"] == case_name:
                datas.remove(data)
                break
        FileHelper.save_json_data(TASK_CASE_FILEPATH, datas)

        print("请求检测服务失败:", str(e))

        return {'current': 0, 'total': 100, 'status': str(e),
                'result': ''}

    # callback demo backend
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': resp.json()}
