import json
import requests


def _get_note_template(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return data


def create_hackmd_note(api_url: str, content: str, header) -> json:

    data = {
        "title": None,
        "content": content,
        "readPermission": "guest",
        "writePermission": "signed_in",
        "commentPermission": "signed_in",
    }
    response = requests.post(api_url, headers=header, json=data)

    print(response)
    # print(response.json())

    return response.json()


def update_hackmd_note(api_url: str, content: str, header) -> str:

    data = {
        "title": None,
        "content": content,
        "readPermission": "guest",
        "writePermission": "signed_in",
    }
    response = requests.patch(api_url, headers=header, json=data)

    print(response)
    # print(response.json())

    return response


def create_collabwriting(note_info: json, template_path: str) -> str:
    return _get_note_template(file_path=template_path).format(
        title=note_info["title"],
        name=note_info["name"],
        slido_1=note_info["Slido"],
        slide_link=note_info["slide"],
    )


def create_collabwriting_toc(template_path: str) -> str:
    return _get_note_template(file_path=template_path)


def create_collabwriting_each_session(
    note_info: json, last_note_info: json, template_path: str
) -> str:
    note_date = ""
    note_time = ""
    note_type = ""
    note_emoji = ""
    note_room = "R" + note_info["Room"]
    note_title = note_info["title"] + " - " + note_info["name"]
    note_hackmd = note_info["HackMD"]

    if note_info["date"] != last_note_info["date"]:
        note_date = "\n# " + note_info["date"] + ""

    if (
        note_info["date"] != last_note_info["date"]
        or note_info["type"] != last_note_info["type"]
        or note_info["begin_time"] != last_note_info["begin_time"]
        or note_info["end_time"] != last_note_info["end_time"]
    ):
        if note_info["type"] != "Talk":
            note_type = " (" + note_info["type"] + ")\n"
        else:
            note_type = "\n"
        note_time = "\n## " + note_info["begin_time"] + " ~ " + note_info["end_time"]

        if note_info["type"] == "Keynote":
            note_emoji = "🔸"

    if note_info["Room"] == "Stage":
        note_room = "R0、R1、R2、R3"

    return _get_note_template(file_path=template_path).format(
        date=note_date,
        time=note_time,
        type=note_type,
        room=note_room,
        emoji=note_emoji,
        title=note_title,
        hackmd=note_hackmd,
    )
