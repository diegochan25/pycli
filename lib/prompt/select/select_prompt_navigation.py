from dataclasses import dataclass
from input.key import Key

@dataclass
class SelectPromptNavigation:
    previous: Key
    next: Key
    select: Key