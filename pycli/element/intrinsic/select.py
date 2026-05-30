from pycli.element.interactive import Interactive
from pycli.input.key import Key
from pycli.styles.style import Style


class Select(Interactive):
    __radio_off = "○"
    __radio_on = "◉"

    index: int
    options: list[str]
    message: str
    required: bool

    def __init__(
        self,
        name: str,
        options: list[str],
        message: str = "Choose an option below:",
        required: bool = False,
    ):
        super().__init__(name)
        self.options = options
        self.message = message
        self.index = 0
        self.required = required
        self.elements = {
            "message": Style(text="bright_black"),
            "option": Style(text="white", before=self.__radio_off),
            "selection": Style(text="blue", before=self.__radio_on),
        }

    def _safe_index(self, index: int) -> None:
        n = len(self.options)
        self.index = index % n if n else 0

    def _draw(self) -> None:
        print(self.elements["message"].format(self.message))
        for i, option in enumerate(self.options):
            key = "selection" if i == self.index else "option"
            print(self.elements[key].format(option))

    def _clear(self) -> None:
        lines = 1 + len(self.options)
        print(f"\033[{lines}A\033[J", end="")

    def navigate(self) -> None:
        key = self.input.get_key()
        if key == Key.ArrowUp:
            self._safe_index(self.index - 1)
        elif key == Key.ArrowDown:
            self._safe_index(self.index + 1)

    def render(self) -> str:
        self._draw()
        while True:
            key = self.input.get_key()
            if key == Key.Enter:
                return self.options[self.index]
            elif key == Key.ArrowUp:
                self._safe_index(self.index - 1)
            elif key == Key.ArrowDown:
                self._safe_index(self.index + 1)
            self._clear()
            self._draw()
