import msvcrt
from input.input_manager import InputManager
from input.key import Key
from input.win32.win32_mapper import Win32Mapper


class Win32Input(InputManager):
    def _mapper(self) -> Win32Mapper:
        return Win32Mapper()

    def get_key(self) -> Key:
        k = msvcrt.getch().decode("latin-1")
        if k in ("\x00", "\xe0"):
            k += msvcrt.getch().decode("latin-1")
        return self._mapper().map(k)

    def get_ln(self) -> str:
        ks = []
        while True:
            k = msvcrt.getch().decode("latin-1")
            if k == "\r":
                break
            ks.append(k)
        return "".join(ks)
