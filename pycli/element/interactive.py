from pycli.element.element import Element
from pycli.input.input_manager import InputManager
from pycli.input.input_manager_factory import InputManagerFactory


class Interactive(Element):
    input: InputManager

    def __init__(self, name: str):
        super().__init__(name)
        self.input = InputManagerFactory.create()

    def navigate(self) -> None:
        pass