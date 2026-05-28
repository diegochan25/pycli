from typing import NoReturn
from pycli.styles.styles import Styles

red = Styles(text="red")

def abort() -> NoReturn:
    print(red.line("\nProgram aborted (Ctrl + C)."))
    exit(1)