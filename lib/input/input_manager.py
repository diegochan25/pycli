from abc import ABC, abstractmethod
from input.input_mapper import InputMapper
from input.key import Key


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
