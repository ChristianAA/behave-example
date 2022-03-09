import json
import os


def get_json_data(relative_path, json_name):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, relative_path + json_name)
    with open(filename) as file:
        data = json.load(file)
        return data
