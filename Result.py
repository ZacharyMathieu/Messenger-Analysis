class Result:
    __data: list[dict[str, int]]
    name: str

    def __init__(self, data: list[dict[str, int]], name: str):
        self.__data = data
        self.name = name

    @staticmethod
    def from_dict(data: dict[str, int], name: str) -> "Result":
        data_list = []
        for key in data:
            data_list.append({key: data[key]})
        return Result(data_list, name)

    def __str__(self):
        s = ""
        for value in self.__data:
            for key in value:
                s += "{} : {}\n".format(key, value[key].__str__())
        return s

    def sort(self):
        # TODO
        return
