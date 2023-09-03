import Constants
from Result import Result


def number_of_messages_by_sender(data: dict[str, any]) -> Result:
    messages = data[Constants.MESSAGES_KEY]
    data = {}

    for d in messages:
        if Constants.SENDER_KEY in d:
            sender = d[Constants.SENDER_KEY]
            if sender in data:
                data[sender] += 1
            else:
                data[sender] = 1

    return Result(data)
