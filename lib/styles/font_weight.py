from typing import Self
from lib.styles.line_style import LineStyle
from lib.styles.style_keys import WeightKey


class FontWeight(LineStyle):
    BOLD = "\x1b[1m"
    DIM = "\x1b[2m"

    @classmethod
    def from_key(cls, key: WeightKey) -> Self:
        return super().from_key(key)