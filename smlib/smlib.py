class NonSquaredLengthException(Exception): pass

def is_sqrt(num) -> bool:
    from math import sqrt
    sqrtt = sqrt(num)
    return sqrtt == round(sqrtt)

def string_to_matrix(string: str) -> list[list[str]]:
    if not is_sqrt(len(string)):
        raise NonSquaredLengthException
    
    from math import sqrt
    l = int(sqrt(len(string)))

    w = []
    c = []
    ind = 0
    for i in range(l):
        for j in range(l):
            c.append(string[ind])
            ind += 1
        w.append(c)
        c = []
    return w



class UnmatchedListLengthException(Exception):
    pass


def objects_to_file( filename: str,  objs: list, *, mode: str = "x", encoding: str = "utf-8-sig") -> None:
    """

        :param filename: the name of the output file
        :param mode: [OPTIONAL] the mode of opening the file, the same you would use for open(), default is creating and writing
        :param objs: MUST HAVE A __names__ FUNCTION AND A __line__ FUNCTION RETURNING STRINGS LIKE THIS: name;name2;name3 AND val1;val2;val3 OTHERWISE IT WILL BREAK!
        :return:
    """
    with open(filename, mode, encoding=encoding) as file:
        file.write(objs[0].__names__())
        file.write("\n")
        for obj in objs:
            file.write(obj.__line__())
            if objs.index(obj) != len(objs) - 1: file.write("\n")


def objects_from_file( filename: str, o_class, *, skip_header = True, encoding: str = "utf-8-sig") -> list:
    """

    :param filename: name of the file that holds the data
    :param o_class: Class that has a VALID CONSTRUCTOR with the EXACT amounts of parameters that the file contains.
    :param skip_header: True if the first line of the file is the names of the values
    :return:
    """
    out = []
    with open(filename, "r", encoding=encoding) as file:
        if skip_header: next(file)

        for line in file:
            data = line.strip().split(";")
            data_stripped = [d.strip() for d in data]
            out.append(o_class(*data_stripped))

    return out

def list_to_file(filename:str, pList: list, *, mode: str = "x", encoding: str = "utf-8-sig", stripData: bool = True) -> None:
    with open(filename, mode, encoding=encoding) as file:
        data = [f"{str(d).strip()}\n" for d in pList] if stripData else [f"{d}\n" for d in pList]
        file.writelines(data)

def lists_to_file(filename:str, pList: list[list], *, mode: str = "x", encoding: str = "utf-8-sig", stripData: bool = True,  ) -> None:
    maxlen = len(pList[0])
    for d in pList:
        if len(d) != maxlen: raise UnmatchedListLengthException(r"All lists should have the sameamount of data/members")
    with open(filename,mode, encoding=encoding) as file:
        for nList in pList:
            for d in range(len(nList)):
                val = str(nList[d])
                if stripData: val = val.strip()
                file.write(f"{nList[d]}")
                file.write(";" if d != len(nList) - 1 else "")

            file.write("\n")
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


if __name__ == "__main__":
    """ from os import remove, path
    if path.exists("test.txt"): remove("test.txt")
    list_to_file("test.txt", [1,2,34,4,5,2])

    with open("test.txt", "r", encoding="utf-8-sig") as test:
        for l in test:print(l,end="")

    input("Enter to delete test output...")
    remove("test.txt") # shit type of tesing bc in a venv the file wont even show up but I'm too lazy to make actual tests

    if path.exists("test.txt"): remove("test.txt")
    lists_to_file("test.txt", [["header", "value"], ["val1", "val3"]])

    with open("test.txt", "r", encoding="utf-8-sig") as test:
        for l in test:print(l,end="")

    input("Enter to delete test output...")
    remove("test.txt") """

    print(string_to_matrix("aaaaaaaaaaaaaaaa"))