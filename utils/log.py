import imp


import json
from datetime import datetime

CURRENT_TIME = datetime.now()


def create_log(log: list) -> None:
    with open(
        "log/" + CURRENT_TIME.strftime("%Y%m%d-%H%M%S") + ".json", "w", encoding="utf-8"
    ) as json_file:
        json.dump(log, json_file, indent=4, separators=(",", ": "))
