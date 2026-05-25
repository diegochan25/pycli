from abc import ABC, abstractmethod
from input.key import Key


class InputMapper(ABC):
    @abstractmethod
    def map(self, seq: str) -> Key:
        pass
