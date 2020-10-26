import json
import os

from app.config import CASE_DATA, TASK_CASE_FILEPATH
from app.libs.file_helper import FileHelper
from app.libs.redprint import Redprint
from app.libs.response import ResultResponse

api = Redprint('cases')


@api.route('', methods=['GET'])
def load_cases():
    """获取案例

    @@@
    #### query参数

    | args | nullable | type | remark |
    |--------|--------|--------|--------|
    #### return
    - ##### json
    > {
        "error_code": 0,
        "msg": "ok",
        "request": "GET /api/cases"
        "data": [
        {
            "casename": "1.3.6.1.4.1.14519.5.2.1.6279.6001.174168737938619557573021395302",
            "filename": "174168737938619557573021395302"
        },
        {
            "casename": "1.3.6.1.4.1.14519.5.2.1.6279.6001.330425234131526435132846006585",
            "filename": "330425234131526435132846006585"
        }]
      }

    #### example
    ```
    url='http://127.0.0.1:5001/api/cases'
    ```
    @@@
    """
    # resp = ResultResponse()
    #
    # case_data = []
    # case_path = "./data/case_data.json"
    # with open(case_path, "r") as fileObj:
    #     case_data = json.load(fileObj, encoding='utf-8')
    #
    # resp.data = case_data

    resp = ResultResponse()
    case_data_path = CASE_DATA + "/data"
    case_seg_path = CASE_DATA + "/seg-lungs-LUNA16"

    match_data = get_match_filenames(case_data_path, case_seg_path)

    case_data = load_json_data(match_data)

    resp.data = case_data

    return resp


@api.route('', methods=['DELETE'])
def clear_cases():
    resp = ResultResponse()
    case_datas = FileHelper.get_json_data(TASK_CASE_FILEPATH)

    for case in case_datas:
        case_datas.remove(case)

    FileHelper.save_json_data(TASK_CASE_FILEPATH, case_datas)

    return resp


def get_filenames(path, suffix='.mhd'):
    filename_list = []

    filenames = os.listdir(path)
    for filename in filenames:
        if os.path.splitext(filename)[1] == suffix:  # 目录下包含.json的文件
            filename_list.append(filename)
    return filename_list


def get_match_filenames(path1, path2):
    list_match = []
    list1 = get_filenames(path1)
    list2 = get_filenames(path2)
    for l1 in list1:
        for l2 in list2:
            if l1 == l2:
                list_match.append(l1)
                break
    return list_match


def load_json_data(list_data):

    case_datas = []
    for data in list_data:
        case_data ={}
        index = data.rindex('.', 0, len(data) - 4)
        case_data["filename"] = data[index + 1: len(data) - 4]
        case_data["casename"] = data[: len(data) - 4]

        case_datas.append(case_data)
    return case_datas
