from uuid import uuid4
import hashlib
from typing import NoReturn
from pycli.styles.styles import Styles

red = Styles(text="red")

def abort() -> NoReturn:
    print(red.line("\nProgram aborted (Ctrl + C)."))
    exit(1)


class Symbol:
    __name: str
    __id: str
    __hash: str


    def __init__(self, name: str):
        self.__name = name
        self.__id = uuid4()
        m = hashlib.sha256()
        m.update(f"{self.__id}{self.__name}".encode())
        self.__hash = m.hexdigest()

    def __str__(self) -> str:
        return self.__name

    def __call__(self) -> str:
        return self.__hash
