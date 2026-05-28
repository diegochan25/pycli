import sys
import tty
import termios
from pycli.input.input_manager import InputManager
from pycli.input.key import Key
from pycli.input.unix.unix_mapper import UnixMapper
from pycli.utils import abort


class UnixInput(InputManager):
    _fd: int
    _saved: list

    def __init__(self):
        self._fd = sys.stdin.fileno()
        self._saved = termios.tcgetattr(self._fd)

    def _mapper(self) -> UnixMapper:
        return UnixMapper()

    def get_key(self) -> Key:
        try:
            tty.setraw(self._fd)
            k = sys.stdin.read(1)
            if k == "\x03":
                abort()
            if k == "\x1b":
                k += sys.stdin.read(2)
            return self._mapper().map(k)
        finally:
            termios.tcsetattr(self._fd, termios.TCSADRAIN, self._saved)

    def getln(self) -> str:
        try:
            termios.tcsetattr(self._fd, termios.TCSADRAIN, self._saved)
            return sys.stdin.readline().rstrip("\n")
        except KeyboardInterrupt:
            abort()
