from abc import ABC, abstractmethod
from lib.input.input_mapper import InputMapper
from lib.input.key import Key


class InputManager(ABC):
    @abstractmethod
    def _mapper(self) -> InputMapper:
        pass

    @abstractmethod
    def get_key(self) -> Key:
        pass

    @abstractmethod
    def get_ln(self) -> str:
        pass
