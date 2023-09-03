import Secrets
from FileReader import FileReader
from MessagesData import MessagesData

# X     Number of messages by sender
#       Number of images by sender
#       Number of characters by sender
#       Most sent message
#       Most used reaction
#       Most used emoji
#       Most used word
#       Average time of day of messages
#       Number of messages by time of day

if __name__ == '__main__':
    messages = MessagesData()

    for file_path in Secrets.DEFAULT_FILES:
        messages.append(FileReader.read(file_path))

    result = messages.number_of_messages_by_sender()
    print(result.__str__())
