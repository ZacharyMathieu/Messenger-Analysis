import Constants
from Result import Result


# X     Number of messages by sender
#       Number of images by sender
#       Number of characters by sender
#       Most sent message
#       Most used reaction
#       Most used emoji
#       Most used word
#       Average time of day of messages
#       Number of messages by time of day

def __count_values_for_key(messages: list[any], key: str) -> Result:
    data: dict[str, int] = {}

    for d in messages:
        if key in d:
            sender = d[key]
            if sender in data:
                data[sender] += 1
            else:
                data[sender] = 1

    return Result.from_dict(data)


def number_of_messages_by_sender(data: dict[str, any]) -> Result:
    return __count_values_for_key(data[Constants.MESSAGES_KEY], Constants.SENDER_KEY)


def most_sent_message(data: dict[str, any]) -> Result:
    return __count_values_for_key(data[Constants.MESSAGES_KEY], Constants.CONTENT_KEY)
