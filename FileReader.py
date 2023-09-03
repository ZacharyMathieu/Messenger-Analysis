import json

import Constants


def read(message_file_path) -> dict[str, any]:
    f = open("./{}/{}".format(Constants.FILES_FOLDER_PATH, message_file_path), "r", encoding="ascii")
    data = json.load(f)

    return data
