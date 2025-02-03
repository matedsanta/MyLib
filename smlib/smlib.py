
def objects_to_file( filename: str,  objs: list, *, mode: str = "x") -> None:
    """

        :param filename: the name of the output file
        :param mode: [OPTIONAL] the mode of opening the file, the same you would use for open(), default is creating and writing
        :param objs: MUST HAVE A __names__ FUNCTION AND A __line__ FUNCTION RETURNING STRINGS LIKE THIS: name;name2;name3 AND val1;val2;val3 OTHERWISE IT WILL BREAK!
        :return:
    """
    with open(filename, mode, encoding="utf-8-sig") as file:
        file.write(objs[0].__names__())
        file.write("\n")
        for obj in objs:
            file.write(obj.__line__())
            if objs.index(obj) != len(objs) - 1: file.write("\n")


def objects_from_file( filename: str, o_class, *, skip_header = True) -> list:
    """

    :param filename: name of the file that holds the data
    :param o_class: Class that has a VALID CONSTRUCTOR with the EXACT amounts of parameters that the file contains. IDGAF about the param names matching, but the NUMBERS MUST
    :param skip_header: self fucking explanatory
    :return:
    """
    out = []
    with open(filename, "r", encoding="utf-8-sig") as file:
        if skip_header: next(file)

        for line in file:
            data = line.strip().split(";")
            data_stripped = [d.strip() for d in data]
            out.append(o_class(*data_stripped))

    return out
