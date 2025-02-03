

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
    :param o_class: Class that has a VALID CONSTRUCTOR with the EXACT amounts of parameters that the file contains.
    :param skip_header: True if the first line of the file is the names of the values
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

from typing import Callable
from re import fullmatch

def default_error():
    print("Wrong input, try again!")

def get_int(in_message: str, error_func: Callable[[], None] = default_error) -> int:
    f = True
    ptrn = r"^-?\d+$"
    inp = ""
    while not fullmatch(ptrn, inp):
        if not f: error_func()
        inp = input(in_message).strip()
        f = False
    return int(inp)


def get_float(in_message: str, error_func: Callable[[], None] = default_error) -> float:
    f = True
    ptrn = r"^-?\d+(\.\d+)?$"
    inp = ""
    while not fullmatch(ptrn, inp):
        if not f: error_func()
        inp = input(in_message).strip()
        f = False
    return float(inp)

def get_email(in_message: str, error_func: Callable[[], None] = default_error) -> str:
    f = True
    ptrn = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    inp = ""
    while not fullmatch(ptrn, inp):
        if not f: error_func()
        inp = input(in_message).strip()
        f = False
    return inp


def get_text(in_message: str, error_func: Callable[[], None] = default_error, *, allow_numbers: bool = False,
             allow_special: bool = False) -> str:
    f = True
    ptrn = r"^[a-zA-Z]+$"

    if allow_numbers and allow_special:
        ptrn = r"^[a-zA-Z0-9!@#$%^&*(),.?\":{}|<>]+$"
    elif allow_numbers:
        ptrn = r"^[a-zA-Z0-9]+$"
    elif allow_special:
        ptrn = r"^[a-zA-Z!@#$%^&*(),.?\":{}|<>]+$"

    inp = ""
    while not fullmatch(ptrn, inp):
        if not f: error_func()
        inp = input(in_message).strip()
        f = False
    return inp


