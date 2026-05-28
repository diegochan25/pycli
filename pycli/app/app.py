from typing import Any, Callable
from pycli.app.branch import Branch

Tree = dict[str, Callable[..., Any] | "Tree"]


class PyCLI:
    __tree: Tree

    def __init__(self):
        self.__tree = {}

    def help(self, fn: Callable[..., Any]) -> Callable[..., Any]:
        print_help = lambda: print(fn())
        self.__tree["help"] = print_help
        self.__tree["--help"] = print_help
        self.__tree["-h"] = print_help

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

    def run(self, args: list[str]) -> None:
        args = args[1:]
        depth = self.__tree
        i = 0

        while i < len(args):
            token = args[i]
            if token not in depth:
                break
            node = depth[token]
            if callable(node):
                node()
                return
            depth = node
            i += 1

        if "help" in self.__tree and callable(self.__tree["help"]):
            print(self.__tree["help"]())