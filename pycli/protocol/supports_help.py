from typing import Protocol


class SupportsHelp(Protocol):
    def help(self, *args, **kwargs) -> str:
        pass
