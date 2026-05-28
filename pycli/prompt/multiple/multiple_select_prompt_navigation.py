from dataclasses import dataclass
from pycli.input.key import Key


@dataclass
class MultipleSelectPromptNavigation:
    previous: Key = Key.ArrowUp
    next: Key = Key.ArrowDown
    toggle: Key = Key.Space
    select: Key = Key.Enter