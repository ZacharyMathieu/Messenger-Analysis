from Result import Result


def write_result(result: Result):
    with open("out/{}.txt".format(result.name), "w", encoding="utf-8") as fout:
        fout.write(result.__str__())
