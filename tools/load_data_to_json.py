import json
import os
import sys


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


def save_json(list_data):
    filename = 'case_data.json'

    case_datas = []
    for data in list_data:
        case_data ={}
        index = data.rindex('.', 0, len(data) - 4)
        case_data["filename"] = data[index + 1: len(data) - 4]
        case_data["casename"] = data[: len(data) - 4]

        case_datas.append(case_data)

    with open(filename, 'w') as file_obj:
        json.dump(case_datas, file_obj, indent=4)


def main(path1, path2):
    list_matches = get_match_filenames(path1, path2)
    save_json(list_matches)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("请输入两个文件夹路径")
    else:
        path1 = sys.argv[1]
        path2 = sys.argv[2]
        print("path1:{}".format(path1))
        print("path2:{}".format(path2))
        main(path1, path2)
