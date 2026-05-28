from dataclasses import dataclass

from pycli.styles.styles import Styles


@dataclass
class MultipleSelectPromptStyles:
    message: Styles = Styles(text="bright_black")
    option: Styles = Styles(text="white")
    selected: Styles = Styles(text="cyan")
    current: Styles = Styles(text="cyan", weight="bold")
