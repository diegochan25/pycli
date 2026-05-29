from dataclasses import dataclass
from pycli.styles.styles import Styles


@dataclass
class NumericPromptStyles:
    message: Styles = Styles(text="bright_black")
    validator: Styles = Styles(text="red", weight="bold")
