from typing import Any, Callable, Type
from pycli.protocol.command import Command
from pycli.utils import Symbol


Tree = dict[str, Callable[..., Any] | "Tree"]

class PyCLI:
    exec = Symbol("exec")
    __tree: Tree

    def __init__(self):
        self.__tree = {}

    def help(self, fn: Callable[..., Any]) -> Callable[..., str]:
        self.__tree["help"] = fn
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    
    def command(self, path: str) -> Callable[..., Type[Command]]:
        def decorator(base_class: Type[Command]) -> Type[Command]:
            fragments = path.split()
            depth = self.__tree
            for part in fragments[:-1]:
                if part not in depth:
                    depth[part] = {}
                depth = depth[part]
            if fragments[-1] in depth and self.exec() in fragments[-1]:
                raise ValueError(f"Command '{path}' already exists.")
            
            depth[fragments[-1]] = {
                "help": base_class.help,
                self.exec(): base_class.exec
            }
            return base_class
        return decorator
    
    def run(self, args: list[str]) -> None:
        exec_key = self.exec()
        depth = self.__tree
        i = 0

        while i < len(args):
            token = args[i]
            if token not in depth:
                break
            next_node = depth[token]
            if isinstance(next_node, dict) and exec_key in next_node:
                next_node[exec_key](*args[i + 1:])
                return
            depth = next_node
            i += 1

        if "help" in self.__tree and callable(self.__tree["help"]):
            self.__tree["help"]()