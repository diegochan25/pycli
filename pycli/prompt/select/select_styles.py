from dataclasses import dataclass

from pycli.styles.styles import Styles


@dataclass
class SelectPromptStyles:
    message: Styles = Styles(text="bright_black")
    option: Styles = Styles(text="white")
    current: Styles = Styles(text="blue")
