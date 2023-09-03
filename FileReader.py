import json

import Constants


class FileReader:
    @staticmethod
    def read(message_file_path) -> dict[str, any]:
        f = open("./{}/{}".format(Constants.FILES_FOLDER_PATH, message_file_path))
        data = json.load(f)

        return data

    @staticmethod
    def decode_accents(message_file_path):
        with open("./{}/{}".format(Constants.FILES_FOLDER_PATH, message_file_path), "rt") as fin:
            with open("out/{}/{}".format(Constants.FILES_FOLDER_PATH, message_file_path), "wt") as fout:
                for line in fin:
                    result_line = line.encode().decode('unicode_escape').__str__()
                    fout.write(result_line)
