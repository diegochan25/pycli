from abc import ABC, abstractmethod
from pycli.input.input_manager import InputManager
from pycli.input.input_manager_factory import InputManagerFactory


class Prompt(ABC):
    input: InputManager

    def __init__(self):
        self.input = InputManagerFactory.create()

    @abstractmethod
    def _draw(self):
        pass

    @abstractmethod
    def render(self):
        pass
