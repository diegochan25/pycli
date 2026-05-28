import sys
from pycli.input.input_manager import InputManager


class InputManagerFactory:
    @classmethod
    def create(cls) -> InputManager:
        if sys.platform == "win32":
            from lib.input.win32.win32_input import Win32Input
            return Win32Input()
        else:
            from pycli.input.unix.unix_input import UnixInput
            return UnixInput()
