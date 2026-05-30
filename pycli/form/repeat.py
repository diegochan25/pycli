from typing import Any
from pycli.protocol.supports_render import SupportsRender


class Repeat:
    def __init__(self, form: SupportsRender, while_: SupportsRender):
        self._form = form
        self._while = while_

    def render(self) -> list[dict[str, Any]]:
        results = []
        while True:
            raw = self._form.render()
            results.append(raw.to_dict() if hasattr(raw, "to_dict") else raw)
            if not self._while.render():
                break
        return results
