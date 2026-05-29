from enum import Enum
from typing import Any
from pycli.prompt.prompt import Prompt
from pycli.pycli.prompt.multiple.multiple_select_navigation import MultipleSelectPromptNavigation
from pycli.prompt.multiple.multiple_select_prompt_styles import MultipleSelectPromptStyles


class MultipleSelectPrompt(Prompt):
    __check_off = "□"
    __check_on = "■"

    __index: int = 0
    __selected: set[int]
    options: list[str]
    _values: list[Any]
    message: str
    navigation: MultipleSelectPromptNavigation
    styles: MultipleSelectPromptStyles

    def __init__(
        self,
        options: type[Enum] | list[str],
        message: str = "Choose all that apply:",
        navigation: MultipleSelectPromptNavigation | None = None,
        styles: MultipleSelectPromptStyles | None = None,
    ):
        super().__init__()
        if isinstance(options, type) and issubclass(options, Enum):
            members = list(options)
            self.options = [str(m.value) for m in members]
            self._values = members
        else:
            self.options = list(options)
            self._values = list(options)
        self.message = message
        self.navigation = navigation if navigation else MultipleSelectPromptNavigation()
        self.styles = styles if styles else MultipleSelectPromptStyles()
        self.__selected = set()

    def __safe_index(self, index: int) -> None:
        if index >= len(self.options):
            self.__index = index % len(self.options)
        elif index < 0:
            self.__index = len(self.options) + index
        else:
            self.__index = index

    def __toggle(self) -> None:
        if self.__index in self.__selected:
            self.__selected.discard(self.__index)
        else:
            self.__selected.add(self.__index)

    def selected_indices(self) -> list[int]:
        return sorted(self.__selected)

    def render(self) -> list[Any]:
        self._draw()
        while True:
            key = self.input.get_key()
            if key == self.navigation.select:
                return [self._values[i] for i in sorted(self.__selected)]
            elif key == self.navigation.toggle:
                self.__toggle()
            elif key == self.navigation.previous:
                self.__safe_index(self.__index - 1)
            elif key == self.navigation.next:
                self.__safe_index(self.__index + 1)
            self._clear()
            self._draw()

    def _clear(self) -> None:
        lines = 1 + len(self.options)
        print(f"\033[{lines}A\033[J", end="")

    def _draw(self) -> None:
        print(self.styles.message.line(self.message))
        for i, option in enumerate(self.options):
            check = self.__check_on if i in self.__selected else self.__check_off
            if i == self.__index:
                print(self.styles.current.line(f"{check} {option}"))
            elif i in self.__selected:
                print(self.styles.selected.line(f"{check} {option}"))
            else:
                print(self.styles.option.line(f"{check} {option}"))