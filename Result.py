class Result:
    __data = {}

    def __init__(self, data):
        self.__data = data

    def __str__(self):
        s = ""
        for key in self.__data:
            s += "{} : {}\n".format(key, self.__data[key].__str__())
        return s
