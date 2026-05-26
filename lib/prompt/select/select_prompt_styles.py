from dataclasses import dataclass

from lib.styles.styles import Styles

@dataclass
class SelectPromptStyles:
    message: Styles
    option: Styles
    selected: Styles