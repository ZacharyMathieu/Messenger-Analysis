import json

import Constants
from MessagesData import MessagesData


class FileReader:
    @staticmethod
    def read(message_file_path) -> MessagesData:
        f = open("./{}/{}".format(Constants.FILES_FOLDER_PATH, message_file_path))
        data = json.load(f)

        return data
