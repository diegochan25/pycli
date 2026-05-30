from dataclasses import dataclass, field
from typing import Any
from pycli.protocol.supports_render import SupportsRender


@dataclass
class ForkResult:
    value: Any
    extra: dict[str, Any] = field(default_factory=dict)


class Fork:
    def __init__(
        self,
        prompt: SupportsRender,
        on: dict[Any, SupportsRender],
        default: SupportsRender | None = None,
    ):
        self._prompt = prompt
        self._on = on
        self._default = default

    def render(self) -> ForkResult:
        value = self._prompt.render()
        sub = self._on.get(value, self._default)
        extra: dict[str, Any] = {}
        if sub is not None:
            raw = sub.render()
            if hasattr(raw, "to_dict"):
                extra = raw.to_dict()
            elif isinstance(raw, dict):
                extra = raw
        return ForkResult(value=value, extra=extra)

