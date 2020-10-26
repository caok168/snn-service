from flask import send_file

from app.config import RESULT_DATA
from app.libs.redprint import Redprint
from app.libs.response import ResultResponse
import base64

api = Redprint('images')


@api.route('/<path>/<name>', methods=['GET'])
def get_image(path, name):
    """获取图片

    @@@
    #### path参数

    | args | nullable | type | remark |
    |--------|--------|--------|--------|
    |    path    |    false    |    string   |    路径名称    |
    |    name    |    false    |    string   |    图片名称    |
    #### return
    - ##### json
    > {
        "error_code": 0,
        "msg": "ok",
        "request": "GET /api/images"
        "data": {"image": ""}
      }

    #### example
    ```
    url='http://127.0.0.1:5001/api/images/<path>/<name>'

    url='http://127.0.0.1:5001/api/images/1.3.6.1.4.1.14519.5.2.1.6279.6001.986011151772797848993829243183/0.jpg'
    ```
    @@@
    """

    image_path = RESULT_DATA

    file_path = '{image_path}/{path}/{name}'.format(image_path=image_path, path=path, name=name)

    return send_file(file_path)

    # resp = ResultResponse()
    # with open(r'{image_path}/{path}/{name}'.format(image_path=image_path, path=path, name=name), 'rb') as f:
    #     base64_data = base64.b64encode(f.read())
    #     s = base64_data.decode()
    # resp.data["image"] = s

    # return resp

