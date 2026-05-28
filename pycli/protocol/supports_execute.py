from typing import Any, Protocol


class SupportsExecute(Protocol):
    def exec(self, *args, **kwargs) -> Any:
        pass
