import json


class FileHelper:
    @staticmethod
    def get_json_data(file_path):
        datas = None
        with open(file_path) as f:
            datas = json.load(f, encoding='utf-8')  # js是转换后的字典

        return datas

    @staticmethod
    def save_json_data(file_path, datas):

        with open(file_path, 'w') as file_obj:
            json.dump(datas, file_obj, indent=4)

