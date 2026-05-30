from typing import Unpack
from pycli.styles.style_args import StyleArgs
from pycli.styles.text_color import TextColor
from pycli.styles.background_color import BackgroundColor
from pycli.styles.font_weight import FontWeight
from pycli.styles.text_decoration import TextDecoration

class Style:
    __reset = "\x1b[0m"

    __before: str
    __after: str

    __prefix: str
    __suffix: str

    def __init__(
        self,
        **kwargs: Unpack[StyleArgs]
    ):
        self.__apply(**kwargs)

    def set(self, **kwargs: Unpack[StyleArgs]) -> None:
        self.__apply(**kwargs)

    def __apply(self, **kwargs: Unpack[StyleArgs]) -> None:
        text = kwargs.get("text")
        bg = kwargs.get("bg")
        weight = kwargs.get("weight")

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
            if kwargs.get(key):
                parts.append(TextDecoration.from_key(key))

        before = kwargs.get("before")
        self.__before = before + " " if before else ""

        after = kwargs.get("after")
        self.__after = " " + after if after else ""

        self.__prefix = "".join(parts)
        self.__suffix = self.__reset if parts else ""

    def format(self, line: str) -> str:
        return f"{self.__prefix}{self.__before}{line}{self.__after}{self.__suffix}"
