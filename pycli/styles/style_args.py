from typing import TypedDict
from pycli.styles.style_keys import ColorKey, WeightKey


class StyleArgs(TypedDict):
    text: ColorKey | None = None
    bg: ColorKey | None = None
    weight: WeightKey | None = None
    italic: bool = False
    underline: bool = False
    blink: bool = False
    invert: bool = False
    hidden: bool = False
    strikethrough: bool = False
    before: str | None
    after: str | None