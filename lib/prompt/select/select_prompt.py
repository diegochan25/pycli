from copy import copy
from input.key import Key
from lib.input.input_manager import InputManager
from lib.prompt.select.select_prompt_navigation import SelectPromptNavigation
from lib.prompt.prompt import Prompt
from lib.prompt.select.select_prompt_styles import SelectPromptStyles
from lib.styles.styles import Styles

class SelectPrompt(Prompt):
    __default_navigation = SelectPromptNavigation(previous=Key.ArrowDown, next=Key.ArrowUp, select=Key.Enter)
    __default_styles = SelectPromptStyles(
        title=Styles(bg='green', text='bright_white', weight='bold'),
        message=Styles(text='bright_black'),
        option=Styles(text='white'),
        selected=Styles(text='blue', weight='bold')
    )
    
    input: InputManager
    options: list[str]
    message: str
    navigation: SelectPromptNavigation
    styles: SelectPromptStyles

    def __init__(
        self,
        options: list[str],
        message: str = "Choose an option below",
        navigation: SelectPromptNavigation | None = None,
        styles: SelectPromptStyles | None = None
    ):
        self.options = options
        self.message = message
        self.navigation = navigation if navigation else copy(self.__default_navigation)
        self.styles = styles if styles else copy(self.__default_styles)

    def ask(self):
        print(self.styles.message.line(self.message))
        print(self.styles.option.line)
