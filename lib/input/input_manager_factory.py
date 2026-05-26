import sys
from lib.input.input_manager import InputManager
from lib.input.unix.unix_input import UnixInput
from lib.input.win32.win32_input import Win32Input


class InputManagerFactory:
    @classmethod
    def get(cls) -> InputManager:
        if sys.platform == "win32":
            return Win32Input()
        else:
            return UnixInput()
