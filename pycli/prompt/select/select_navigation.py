from dataclasses import dataclass
from pycli.input.key import Key


@dataclass
class SelectPromptNavigation:
    previous: Key = Key.ArrowUp
    next: Key = Key.ArrowDown
    select: Key = Key.Enter