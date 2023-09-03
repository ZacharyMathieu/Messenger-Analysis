from datetime import datetime, timezone, timedelta
from typing import Callable

import Constants
from Result import Result


# X     Number of messages by sender
#       Number of images by sender
# X     Number of characters by sender
# X     Most sent message
#       Most used reaction
#       Most used emoji
# X     Most used word
# X     Average time of day of messages
# X     Number of messages by time of day

def __count_values_for_key(messages: list[any], key: str, name: str) -> Result:
    data: dict[str, int] = {}

    for d in messages:
        if key in d:
            value = d[key]
            if value in data:
                data[value] += 1
            else:
                data[value] = 1

    return Result.from_dict(data, name)


def number_of_messages_by_sender(data: dict[str, any]) -> Result:
    return __count_values_for_key(data[Constants.MESSAGES_KEY], Constants.SENDER_KEY, "Number of messages by sender")


def number_of_messages_by_message_content(data: dict[str, any]) -> Result:
    return __count_values_for_key(data[Constants.MESSAGES_KEY], Constants.CONTENT_KEY,
                                  "Number of messages by message content")


def number_of_characters_by_sender(data: dict[str, any]) -> Result:
    result: dict[str, int] = {}
    messages = data[Constants.MESSAGES_KEY]
    name = "Number of characters by sender"

    for message in messages:
        if Constants.CONTENT_KEY in message and Constants.SENDER_KEY in message:
            sender = message[Constants.SENDER_KEY]

            if sender not in result:
                result[sender] = 0

            result[sender] += len(message[Constants.CONTENT_KEY])

    return Result.from_dict(result, name)


def most_used_word(data: dict[str, any]) -> Result:
    messages = data[Constants.MESSAGES_KEY]
    key = Constants.CONTENT_KEY
    name = "Most used word"

    data: dict[str, int] = {}

    for d in messages:
        if key in d:
            message: str = d[key]
            # words = message.lower() \
            words = message \
                .replace(".", "") \
                .replace(",", "") \
                .replace("'", " ") \
                .split(" ")
            for word in words:
                if word in data:
                    data[word] += 1
                else:
                    data[word] = 1

    return Result.from_dict(data, name)


def average_time_of_day_of_messages(data: dict[str, any]) -> Result:
    messages = data[Constants.MESSAGES_KEY]
    key = Constants.TIMESTAMP_KEY
    name = "Average time of day of messages"

    data: dict[str, float] = {}

    total: float = 0
    count: int = 0
    for d in messages:
        if key in d:
            timestamp: int = d[key]

            datetime_value = datetime.fromtimestamp(timestamp / 1000, tz=timezone(timedelta(hours=-4)))
            seconds_past_midnight = (datetime_value.hour * 3600) + (datetime_value.minute * 60) + datetime_value.second

            total += seconds_past_midnight
            count += 1

    data["Total"] = total
    data["Count"] = count

    average = total / count
    data["Average"] = average

    datetime_average = datetime.fromtimestamp(average)
    data["Average Hour"] = datetime_average.hour
    data["Average Minute"] = datetime_average.minute
    data["Average Second"] = datetime_average.second

    return Result.from_dict(data, name)


def __number_of_messages_by_time_of_day(data: dict[str, any],
                                        to_time_of_day: Callable[[datetime], str],
                                        name: str) -> Result:
    messages = data[Constants.MESSAGES_KEY]
    key = Constants.TIMESTAMP_KEY

    data: dict[str, float] = {}

    for d in messages:
        if key in d:
            timestamp: int = d[key]

            datetime_value = datetime.fromtimestamp(timestamp / 1000, tz=timezone(timedelta(hours=-4)))

            time_of_day = to_time_of_day(datetime_value)

            if time_of_day in data:
                data[time_of_day] += 1
            else:
                data[time_of_day] = 1

    return Result.from_dict(data, name)


def number_of_messages_by_time_of_day_hours(data: dict[str, any]) -> Result:
    return __number_of_messages_by_time_of_day(
        data,
        lambda t: "{}".format(t.hour),
        "Number of messages by time of day (hours)"
    )


def number_of_messages_by_time_of_day_minutes(data: dict[str, any]) -> Result:
    return __number_of_messages_by_time_of_day(
        data,
        lambda t: "{}:{}".format(t.hour, t.minute),
        "Number of messages by time of day (minutes)"
    )


def number_of_messages_by_time_of_day_seconds(data: dict[str, any]) -> Result:
    return __number_of_messages_by_time_of_day(
        data,
        lambda t: "{}:{}:{}".format(t.hour, t.minute, t.second),
        "Number of messages by time of day (seconds)"
    )
