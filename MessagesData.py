import Constants
from Result import Result


class MessagesData:
    __data = []

    def __init__(self):
        self.__data = {Constants.MESSAGES_KEY: []}

    def __str__(self):
        s = ""
        for d in self.__data[Constants.MESSAGES_KEY]:
            if Constants.SENDER_KEY in d \
                    and Constants.TIMESTAMP_KEY in d \
                    and Constants.CONTENT_KEY in d:
                s += "sender: {}\ntime: {}\ncontent: {}\n\n" \
                    .format(d[Constants.SENDER_KEY],
                            d[Constants.TIMESTAMP_KEY],
                            d[Constants.CONTENT_KEY])
        return s

    @staticmethod
    def from_raw_data() -> "MessagesData":
        return 
    def __get_messages(self):
        return self.__data[Constants.MESSAGES_KEY]

    def append(self, data: "MessagesData"):
        self.__data[Constants.MESSAGES_KEY].append(data.__get_messages)

    def number_of_messages_by_sender(self) -> Result:
        data = {}
        for d in self.__data[Constants.MESSAGES_KEY]:
            if Constants.SENDER_KEY in d:
                sender = d[Constants.SENDER_KEY]
                if sender in data:
                    data[sender] += 1
                else:
                    data[sender] = 1
        return Result(data)
