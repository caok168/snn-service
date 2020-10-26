# from celery import Celery
# # from app import create_app
# from app.libs.error_code import ServiceError
# from app.libs.request_helper import RequestHelper
#
# # app = create_app()
#
# celery = Celery('test', broker='redis://localhost:6380/0')
# # celery.conf.update(app.config)
#
#
# @celery.task(bind=True)
# def detect_task(self, case_name):
#     print(case_name)
#
#     url_base = 'http://192.168.11.17:9090'
#
#     # mhd_file = "data/1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860.mhd"
#     # seg_file = "seg-lungs-LUNA16/1.3.6.1.4.1.14519.5.2.1.6279.6001.100225287222365663678666836860.mhd"
#
#     mhd_file = "data/{}.mhd".format(case_name)
#     seg_file = "seg-lungs-LUNA16/{}.mhd".format(case_name)
#
#     url = url_base + '/api/v1/detect/ct-detect-save'
#     callback = "/tasks/{task_id}/progress".format(task_id=self.request.id)
#     print("callback=", callback)
#
#     data = {
#         "mhd_file": mhd_file,
#         "seg_file": seg_file,
#         "callback": callback,
#     }
#
#     try:
#         resp = RequestHelper().post(url, data)
#         resp.raise_for_status()
#     except Exception:
#         raise ServiceError()
#
#     # callback demo backend
#     return {'current': 100, 'total': 100, 'status': 'Task completed!',
#             'result': resp.json()}
