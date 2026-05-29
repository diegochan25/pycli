from typing import Any
from pycli.protocol.supports_render import SupportsRender
from pycli.form.result import Result
from pycli.form.branch import BranchResult


class Form:
    def __init__(self, **fields: SupportsRender):
        self._fields = fields

    def render(self) -> Result:
        data: dict[str, Any] = {}
        for name, field in self._fields.items():
            result = field.render()
            if isinstance(result, BranchResult):
                if result.value is not None:
                    data[name] = result.value
                data.update(result.extra)
            elif result is not None:
                data[name] = result
        return Result(data)
