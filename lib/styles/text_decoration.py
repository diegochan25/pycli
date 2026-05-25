from typing import Self
from styles.line_style import LineStyle
from styles.style_keys import DecorationKey

class TextDecoration(LineStyle):
    ITALIC = "\x1b[3m"
    UNDERLINE = "\x1b[4m"
    BLINK = "\x1b[5m"
    INVERT = "\x1b[7m"
    HIDDEN = "\x1b[8m"
    STRIKETHROUGH = "\x1b[9m"

    @classmethod
    def from_key(cls, key: DecorationKey) -> Self:
        return super().from_key(key)