import FileReader
import Secrets
import Strategies
from MessagesData import MessagesData

if __name__ == '__main__':
    messages = MessagesData()

    for file_path in Secrets.DEFAULT_FILES:
        messages.append(FileReader.read(file_path))

    messages.apply_strategy(Strategies.number_of_messages_by_sender, sort=True, write_result=True)
    messages.apply_strategy(Strategies.number_of_messages_by_message_content, sort=True, write_result=True)
