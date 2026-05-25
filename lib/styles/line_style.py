from enum import StrEnum
from typing import Self


class LineStyle(StrEnum):
    @classmethod
    def from_key(cls, key: str) -> Self:
        """
        Returns the enum member represented by key.

        Args:
            key (K): the key representation of the enum member
            to retrieve.
        Returns:
            The enum member corresponding to the provided key.
        Raises:
            KeyError: if the provided key cannot be mapped to
            an existing enum member.
        """
        return cls[key.upper()]