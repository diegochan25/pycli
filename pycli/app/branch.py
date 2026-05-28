from typing import Any, Callable

Tree = dict[str, Callable[..., Any] | "Tree"]


class Branch:
    __prefix: str
    __aliases: list[str]
    __leaves: Tree

    def __init__(self, prefix: str, *aliases):
        self.__prefix = prefix
        self.__aliases = aliases
        self.__leaves = {}

    @property
    def prefix(self) -> str:
        return self.__prefix
    
    @property
    def aliases(self) -> str:
        return self.__aliases

    def leaf(self, name: str, *aliases: str) -> Callable[..., Callable[..., Any]]:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            for key in (name, *aliases):
                if key in self.__leaves:
                    raise ValueError(
                        f"Leaf '{key}' already exists in branch '{self.__prefix}'."
                    )
            for key in (name, *aliases):
                self.__leaves[key] = fn
            return fn

        return decorator

    def use(self, branch: "Branch") -> None:
        prefix = branch.prefix
        aliases = branch.aliases
        for cmd in (prefix, *aliases):
            if cmd in self.__leaves:
                raise ValueError(f"Branch '{cmd}' is already mounted.")
            self.__leaves[cmd] = branch._leaves()

    def _leaves(self) -> Tree:
        return self.__leaves
