import Secrets
import Strategies
from FileReader import FileReader
from MessagesData import MessagesData


if __name__ == '__main__':
    messages = MessagesData()

    for file_path in Secrets.DEFAULT_FILES:
        messages.append(FileReader.read(file_path))

    result = messages.apply_strategy(Strategies.number_of_messages_by_sender)
    print(result.__str__())
