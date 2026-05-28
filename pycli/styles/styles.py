from pycli.styles.style_keys import ColorKey, WeightKey
from pycli.styles.text_color import TextColor
from pycli.styles.background_color import BackgroundColor
from pycli.styles.font_weight import FontWeight
from pycli.styles.text_decoration import TextDecoration


class Styles:
    __reset = "\x1b[0m"

    __prefix: str
    __suffix: str

    def __init__(
        self,
        text: ColorKey | None = None,
        bg: ColorKey | None = None,
        weight: WeightKey | None = None,
        italic: bool = False,
        underline: bool = False,
        blink: bool = False,
        invert: bool = False,
        hidden: bool = False,
        strikethrough: bool = False,
    ):
        parts: list[str] = []

        if text:
            parts.append(TextColor.from_key(text))
        if bg:
            parts.append(BackgroundColor.from_key(bg))
        if weight:
            parts.append(FontWeight.from_key(weight))

        for key in (
            "italic",
            "underline",
            "blink",
            "invert",
            "hidden",
            "strikethrough",
        ):
            if locals()[key]:
                parts.append(TextDecoration.from_key(key))

        self.__prefix = "".join(parts)
        self.__suffix = self.__reset if parts else ""

    def line(self, line: str) -> str:
        return f"{self.__prefix}{line}{self.__suffix}"

    def lines(self, *lines: str) -> str:
        return f"{self.__prefix}{'\n'.join(lines)}{self.__suffix}"
