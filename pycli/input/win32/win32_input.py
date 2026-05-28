import msvcrt
from pycli.input.input_manager import InputManager
from pycli.input.key import Key
from pycli.input.win32.win32_mapper import Win32Mapper
from pycli.utils import abort


class Win32Input(InputManager):
    def _mapper(self) -> Win32Mapper:
        return Win32Mapper()

    def get_key(self) -> Key:
        k = msvcrt.getch().decode("latin-1")
        if k == "\x03":
            abort()
        if k in ("\x00", "\xe0"):
            k += msvcrt.getch().decode("latin-1")
        return self._mapper().map(k)

    def getln(self) -> str:
        ks = []
        while True:
            k = msvcrt.getch().decode("latin-1")
            if k == "\r":
                break
            ks.append(k)
        return "".join(ks)
