from typing import Any


class FormData:
    def __init__(self):
        object.__setattr__(self, "_data", {})

    def __getattr__(self, name: str) -> Any:
        data = object.__getattribute__(self, "_data")
        try:
            return data[name]
        except KeyError:
            raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    def __setattr__(self, name: str, value: Any) -> None:
        object.__getattribute__(self, "_data")[name] = value

    def to_dict(self) -> dict:
        return dict(object.__getattribute__(self, "_data"))

    def __repr__(self) -> str:
        return f"FormData({object.__getattribute__(self, '_data')})"
