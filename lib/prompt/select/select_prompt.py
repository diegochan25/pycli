from copy import copy
from input.key import Key
from prompt.select.select_prompt_navigation import SelectPromptNavigation
from prompt.prompt import Prompt
from prompt.select.select_prompt_styles import SelectPromptStyles
from styles.styles import Styles

class SelectPrompt(Prompt):
    __default_navigation = SelectPromptNavigation(previous=Key.ArrowDown, next=Key.ArrowUp, select=Key.Enter)
    __default_styles = SelectPromptStyles(
        title=Styles(bg='green', text='bright_white', weight='bold'),
        message=Styles(text='bright_black'),
        option=Styles(text='white'),
        selected=Styles(text='blue', weight='bold')
    )
    
    navigation: SelectPromptNavigation
    styles: SelectPromptStyles

    def __init__(
        self, 
        navigation: SelectPromptNavigation | None = None,
        styles: SelectPromptStyles | None = None
    ):
        self.navigation = navigation if navigation else copy(self.__default_navigation)
        self.styles = styles if styles else copy(self.__default_styles)
