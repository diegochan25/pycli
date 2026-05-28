from abc import ABC, abstractmethod
from pycli.input.input_mapper import InputMapper
from pycli.input.key import Key


class InputManager(ABC):
    @abstractmethod
    def _mapper(self) -> InputMapper:
        pass

    @abstractmethod
    def get_key(self) -> Key:
        pass

    @abstractmethod
    def getln(self) -> str:
        pass
