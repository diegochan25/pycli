from typing import Any
from pycli.styles.style import Style


class Element:
    name: str
    elements: dict[str, Style]

    def __init__(self, name: str):
        self.name = name
        self.elements = {}

    def __getattr__(self, name):
        attr = self.elements.get(name)
        if attr is None:
            raise AttributeError(f"Object '{self.__class__.__name__}' has no attribute '{name}'")
        return attr

    def render(self) -> Any:
        pass
