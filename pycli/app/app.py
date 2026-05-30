import sys

from pycli.utils import Symbol
from typing import Any, Callable
from pycli.app.branch import Branch

Tree = dict[str, Callable[..., Any] | "Tree"]


class PyCLI:
    h = Symbol("help") 
    __tree: Tree

    def __init__(self):
        self.__tree = {}

    @classmethod
    def __to_namespace(cls, args: list[str]) -> dict[str, Any]:
        argd = {}
        key = ""
        for arg in args:
            if arg.startswith("-"):
                key = arg.replace("-", "_").lstrip("_")
                argd[key] = []
            elif key:
                argd[key].append(arg)

        for key, value in argd.items():
            if not value:
                argd[key] = True
            elif len(value) == 1:
                argd[key] = value[0]
        return argd

    def help(self, fn: Callable[..., Any]) -> Callable[..., Any]:
        self.__tree[self.h()] = fn
        self.__tree["--help"] = fn
        self.__tree["-h"] = fn

        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)

        return wrapper

    def leaf(self, name: str, *aliases: str) -> Callable[..., Callable[..., Any]]:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            for key in (name, *aliases):
                if key in self.__tree:
                    raise ValueError(f"Leaf '{key}' already exists.")
            for key in (name, *aliases):
                self.__tree[key] = fn
            return fn

        return decorator

    def use(self, branch: Branch) -> None:
        prefix = branch.prefix
        aliases = branch.aliases
        for cmd in [prefix, *aliases]:
            if cmd in self.__tree:
                raise ValueError(f"Branch '{cmd}' is already mounted.")
            self.__tree[cmd] = branch._leaves()

    def run(self) -> None:
        args = sys.argv[1:]
        depth = self.__tree
        i = 0

        while i < len(args):
            token = args[i]
            if token not in depth:
                break
            node = depth[token]
            if callable(node):
                node().render()
                return
            depth = node
            i += 1

        if self.h() in self.__tree and callable(self.__tree[self.h()]):
            self.__tree[self.h()]().render()