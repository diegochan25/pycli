from abc import ABC, abstractmethod
from lib.input.key import Key


class InputMapper(ABC):
    @abstractmethod
    def map(self, seq: str) -> Key:
        pass
