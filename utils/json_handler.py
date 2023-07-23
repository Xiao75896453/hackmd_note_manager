import json


def read_json(file_name: str) -> json:
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
