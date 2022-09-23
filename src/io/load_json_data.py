import json


def load(file_name):
    with open(file_name, 'r', encoding='utf-8') as load_f:
        data = json.load(load_f)
        # print(data)
        return data
