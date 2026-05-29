from typing import Any
from pycli.protocol.supports_render import SupportsRender


class Repeat:
    def __init__(self, form: SupportsRender, while_: SupportsRender):
        self._form = form
        self._while = while_

    def render(self) -> list[dict[str, Any]]:
        from pycli.form.result import Result

        results = []
        while True:
            raw = self._form.render()
            results.append(raw.to_dict() if isinstance(raw, Result) else raw)
            if not self._while.render():
                break
        return results
