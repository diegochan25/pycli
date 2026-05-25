from dataclasses import dataclass

from styles.styles import Styles

@dataclass
class SelectPromptStyles:
    title: Styles
    message: Styles
    option: Styles
    selected: Styles