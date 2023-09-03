import FileReader
import Secrets
import Strategies
from MessagesData import MessagesData

if __name__ == '__main__':
    messages = MessagesData()

    for file_path in Secrets.DEFAULT_FILES:
        messages.append(FileReader.read(file_path))

    # messages.apply_strategy(Strategies.number_of_messages_by_sender, sort=True, write_result=True)
    # messages.apply_strategy(Strategies.number_of_messages_by_message_content, sort=True, write_result=True)
    # messages.apply_strategy(Strategies.most_used_word, sort=True, write_result=True)
    # messages.apply_strategy(Strategies.average_time_of_day_of_messages, sort=False, write_result=True)
    # messages.apply_strategy(Strategies.number_of_messages_by_time_of_day_hours, sort=True, write_result=True)
    # messages.apply_strategy(Strategies.number_of_messages_by_time_of_day_minutes, sort=True, write_result=True)
    # messages.apply_strategy(Strategies.number_of_messages_by_time_of_day_seconds, sort=True, write_result=True)
