from typing import Any
from pycli.protocol.supports_render import SupportsRender


class Fieldset:
    title: str
    _fields: dict[str, SupportsRender]

    def __init__(self, title: str, **fields: SupportsRender):
        self.title = title
        self._fields = fields

    def render(self) -> dict[str, Any] | None:
        print(self.title)
        if not self._fields:
            return None
        results: dict[str, Any] = {}
        for name, field in self._fields.items():
            result = field.render()
            if result is not None:
                results[name] = result
        return results or None
