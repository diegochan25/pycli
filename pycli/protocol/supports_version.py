from typing import Protocol


class SupportsVersion(Protocol):
    _version: tuple[int, int, int] | None = None
    @property
    def version(self) -> str:
        if self._version is None:
            raise NotImplementedError("version property must be implemented")
        return f"{self._version[0]}.{self._version[1]}.{self._version[2]}"