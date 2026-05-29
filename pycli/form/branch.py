from dataclasses import dataclass, field
from typing import Any
from pycli.protocol.supports_render import SupportsRender


@dataclass
class BranchResult:
    value: Any
    extra: dict[str, Any] = field(default_factory=dict)


class Branch:
    def __init__(
        self,
        prompt: SupportsRender,
        on: dict[Any, SupportsRender],
        default: SupportsRender | None = None,
    ):
        self._prompt = prompt
        self._on = on
        self._default = default

    def render(self) -> BranchResult:
        from pycli.form.result import Result

        value = self._prompt.render()
        sub = self._on.get(value, self._default)
        extra: dict[str, Any] = {}
        if sub is not None:
            raw = sub.render()
            if isinstance(raw, Result):
                extra = raw.to_dict()
            elif isinstance(raw, dict):
                extra = raw
        return BranchResult(value=value, extra=extra)
