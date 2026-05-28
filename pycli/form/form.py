from typing import Any
from pycli.protocol.supports_render import SupportsRender
from pycli.form.result import Result


class Form:
    _fields: dict[str, SupportsRender]

    def __init__(self, **fields: SupportsRender):
        self._fields = fields

    def render(self) -> Result:
        data: dict[str, Any] = {}
        for name, field in self._fields.items():
            result = field.render()
            if result is not None:
                data[name] = result
        return Result(data)
