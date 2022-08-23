import os

from dotenv import load_dotenv


from utils.csv_handler import read_csv, write_csv
from utils.log import create_log
from utils.note import (
    create_collabwriting,
    create_collabwriting_toc,
    create_collabwriting_each_session,
    create_hackmd_note,
)

load_dotenv()

TEAM_PATH = os.getenv("TEAM_PATH")
TOKEN = os.getenv("TOKEN")
HACKMD_API_URL = os.getenv("HACKMD_API_URL")

HEADER = {"Authorization": "Bearer " + TOKEN}
TEMPLATE_PATH = "note_template/pycon_apac_2022/"
NOTE_DATA_PATH = "note_data/"
OUTPUT_PATH = "output/"

API_URL_CREATE_USER_NOTE = HACKMD_API_URL + "notes"
API_URL_CREATE_TEAM_NOTE = HACKMD_API_URL + "teams/" + TEAM_PATH + "/notes"


if __name__ == "__main__":
    note_data_file_name = "WIP_ 2022 Pre-CFP empty schedule.csv"
    note_data_file_path = NOTE_DATA_PATH + note_data_file_name
    note_data_info = read_csv(file_path=note_data_file_path)

    notes_title = note_data_info["title"]
    notes_info = note_data_info["data"]

    notes_info.sort(key=lambda x: (x["date"], x["begin_time"], x["type"], x["Room"]))

    log = []

    collabwriting_template_path = TEMPLATE_PATH + "collabwriting.md"
    collabwriting_toc_template_path = TEMPLATE_PATH + "collabwriting_toc.md"
    collabwriting_each_session_template_path = TEMPLATE_PATH + "each_session.md"
    collabwriting_toc_content = create_collabwriting_toc(
        template_path=collabwriting_toc_template_path
    )

    last_note_info = {}
    for title in notes_title:
        last_note_info[title] = ""

    for note_info in notes_info:
        collabwriting_content = create_collabwriting(
            note_info=note_info, template_path=collabwriting_template_path
        )

        # make_team_collabwriting = create_hackmd_note(
        #     api_url=API_URL_CREATE_TEAM_NOTE,
        #     content=collabwriting_content,
        #     header=HEADER,
        # )
        # hackmd_link = make_team_collabwriting["publishLink"]
        # note_info["HackMD"] = hackmd_link
        # log.append(make_team_collabwriting)

        collabwriting_toc_content += create_collabwriting_each_session(
            note_info=note_info,
            last_note_info=last_note_info,
            template_path=collabwriting_each_session_template_path,
        )

        last_note_info = note_info

    # make_team_collabwriting_toc = create_hackmd_note(
    #     api_url=API_URL_CREATE_TEAM_NOTE,
    #     content=collabwriting_toc_content,
    #     header=HEADER,
    # )
    # hackmd_link = make_team_collabwriting_toc["publishLink"]
    # note_info["HackMD"] = hackmd_link
    # log.append(make_team_collabwriting_toc)

    print(collabwriting_toc_content)
    create_log(log)

    output_file_name = "WIP_ 2022 Pre-CFP empty schedule.csv"
    output_file_path = OUTPUT_PATH + output_file_name
    write_csv(file_path=output_file_path, title_items=notes_title, datas=notes_info)
