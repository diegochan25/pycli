from typing import Self
from pycli.styles.line_style import LineStyle
from pycli.styles.style_keys import ColorKey


class BackgroundColor(LineStyle):
    BLACK = "\x1b[40m"
    RED = "\x1b[41m"
    GREEN = "\x1b[42m"
    YELLOW = "\x1b[43m"
    BLUE = "\x1b[44m"
    MAGENTA = "\x1b[45m"
    CYAN = "\x1b[46m"
    WHITE = "\x1b[47m"
    BRIGHT_BLACK = "\x1b[100m"
    BRIGHT_RED = "\x1b[101m"
    BRIGHT_GREEN = "\x1b[102m"
    BRIGHT_YELLOW = "\x1b[103m"
    BRIGHT_BLUE = "\x1b[104m"
    BRIGHT_MAGENTA = "\x1b[105m"
    BRIGHT_CYAN = "\x1b[106m"
    BRIGHT_WHITE = "\x1b[107m"

    @classmethod
    def from_key(cls, key: ColorKey) -> Self:
        return super().from_key(key)
