import csv
import json


def read_csv(file_path: str) -> json:

    data = []
    with open(file_path, "r", encoding="utf-8-sig") as file:
        csvreader = list(csv.reader(file))

        title = csvreader.pop(0)

        for row in csvreader:
            row_json = {}
            for i in range(len(title)):
                try:
                    row_json[title[i]] = row[i]
                except:
                    row_json[title[i]] = ""
            data.append(row_json)

        return {"title": title, "data": data}


def write_csv(file_path: str, title_items: list, datas: list):

    with open(file_path, "w", newline="") as f:
        title = title_items
        cw = csv.DictWriter(f, title, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        cw.writeheader()
        cw.writerows(datas)
