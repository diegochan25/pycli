from pycli.prompt.prompt import Prompt
from pycli.prompt.select.select_prompt_navigation import SelectPromptNavigation
from pycli.prompt.select.select_prompt_styles import SelectPromptStyles


class SelectPrompt(Prompt):
    __radio_off = "○"
    __radio_on = "◉"

    __index: int = 0
    options: list[str]
    message: str
    navigation: SelectPromptNavigation
    styles: SelectPromptStyles

    def __init__(
        self,
        options: list[str],
        message: str = "Choose an option below:",
        navigation: SelectPromptNavigation | None = None,
        styles: SelectPromptStyles | None = None,
    ):
        super().__init__()
        self.options = options
        self.message = message
        self.navigation = navigation if navigation else SelectPromptNavigation()
        self.styles = styles if styles else SelectPromptStyles()

    def __safe_index(self, index: int) -> None:
        if index >= len(self.options):
            self.__index = index % len(self.options)
        elif index < 0:
            self.__index = len(self.options) + index
        else:
            self.__index = index

    def render(self) -> str:
        self._draw()
        while True:
            key = self.input.get_key()
            if key == self.navigation.select:
                return self.options[self.__index]
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
            if i == self.__index:
                print(self.styles.current.line(f"{self.__radio_on} {option}"))
            else:
                print(self.styles.option.line(f"{self.__radio_off} {option}"))
