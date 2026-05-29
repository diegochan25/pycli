from typing import Any


class Result:
    _result: dict[str, Any]

    def __init__(self, result: dict[str, Any] | None = None):
        object.__setattr__(self, "_result", result if result is not None else {})

    def __getattr__(self, name) -> Any:
        attr = self._result.get(name, None)
        if attr is None:
            raise AttributeError(f"'{self.__class__.__name__}' object has no attribute '{name}'")
        return attr
    
    def __getitem__(self, key):
        return self._result[key]
    
    def get(self, key: str, default: Any = None) -> Any:
        return self._result.get(key, default)

    def to_dict(self) -> dict[str, Any]:
        return dict(self._result)