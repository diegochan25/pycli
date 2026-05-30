from typing import Any, Callable
from pycli.element.element import Element
from pycli.styles.style import Style

Tree = dict[str, Callable[..., Any] | "Tree"]


class Help(Element):
    __tree: Tree

    def __init__(self, name: str, tree: Tree | None = None):
        super().__init__(name)
        self.__tree = tree or {}
        self.elements = {
            "header": Style(text="bright_white", weight="bold"),
            "cmd": Style(text="cyan"),
            "group": Style(text="yellow", weight="bold"),
            "sub": Style(text="cyan"),
        }

    def render(self) -> None:
        visible = {
            k: v
            for k, v in self.__tree.items()
            if isinstance(k, str) and not k.startswith("-")
        }
        if not visible:
            return

        print(self.elements["header"].format("Commands:"))
        for name, node in visible.items():
            if callable(node):
                print(f"  {self.elements['cmd'].format(name)}")
            else:
                print(f"  {self.elements['group'].format(name)}")
                for sub, val in node.items():
                    if isinstance(sub, str) and not sub.startswith("-") and callable(val):
                        print(f"    {self.elements['sub'].format(sub)}")
