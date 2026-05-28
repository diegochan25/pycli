from dataclasses import dataclass
from pycli.styles.styles import Styles


@dataclass
class OutputStyles:
    message: Styles = Styles()
