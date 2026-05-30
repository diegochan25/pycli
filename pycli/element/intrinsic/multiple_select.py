from pycli.element.interactive import Interactive
from pycli.input.key import Key
from pycli.styles.style import Style


class MultipleSelect(Interactive):
    __check_off = "□"
    __check_on = "■"

    index: int
    options: list[str]
    message: str

    def __init__(
        self,
        name: str,
        options: list[str],
        message: str = "Choose all that apply:",
    ):
        super().__init__(name)
        self.options = options
        self.message = message
        self.index = 0
        self.__selected: set[int] = set()
        self.elements = {
            "message": Style(text="bright_black"),
            "option": Style(text="white"),
            "selected": Style(text="cyan"),
            "current": Style(text="cyan", weight="bold"),
        }

    def _safe_index(self, index: int) -> None:
        n = len(self.options)
        self.index = index % n if n else 0

    def _toggle(self) -> None:
        if self.index in self.__selected:
            self.__selected.discard(self.index)
        else:
            self.__selected.add(self.index)

    def _draw(self) -> None:
        print(self.elements["message"].format(self.message))
        for i, option in enumerate(self.options):
            check = self.__check_on if i in self.__selected else self.__check_off
            if i == self.index:
                print(self.elements["current"].format(f"{check} {option}"))
            elif i in self.__selected:
                print(self.elements["selected"].format(f"{check} {option}"))
            else:
                print(self.elements["option"].format(f"{check} {option}"))

    def _clear(self) -> None:
        lines = 1 + len(self.options)
        print(f"\033[{lines}A\033[J", end="")

    def navigate(self) -> None:
        key = self.input.get_key()
        if key == Key.ArrowUp:
            self._safe_index(self.index - 1)
        elif key == Key.ArrowDown:
            self._safe_index(self.index + 1)
        elif key == Key.Space:
            self._toggle()

    def render(self) -> list[str]:
        self._draw()
        while True:
            key = self.input.get_key()
            if key == Key.Enter:
                return [self.options[i] for i in sorted(self.__selected)]
            elif key == Key.ArrowUp:
                self._safe_index(self.index - 1)
            elif key == Key.ArrowDown:
                self._safe_index(self.index + 1)
            elif key == Key.Space:
                self._toggle()
            self._clear()
            self._draw()
