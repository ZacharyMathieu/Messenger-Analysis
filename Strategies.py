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

def __count_values_for_key(messages: list[any], key: str, name: str) -> Result:
    data: dict[str, int] = {}

    for d in messages:
        if key in d:
            sender = d[key]
            if sender in data:
                data[sender] += 1
            else:
                data[sender] = 1

    return Result.from_dict(data, name)


def number_of_messages_by_sender(data: dict[str, any]) -> Result:
    return __count_values_for_key(data[Constants.MESSAGES_KEY], Constants.SENDER_KEY, "Number of messages by sender")


def number_of_messages_by_message_content(data: dict[str, any]) -> Result:
    return __count_values_for_key(data[Constants.MESSAGES_KEY], Constants.CONTENT_KEY,
                                  "Number of messages by message content")
