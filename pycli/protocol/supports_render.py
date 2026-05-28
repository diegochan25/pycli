from typing import Any, Protocol


class SupportsRender(Protocol):
    def render(self) -> Any:
        pass
