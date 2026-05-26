from abc import ABC, abstractmethod


class Prompt(ABC):
    @abstractmethod
    def ask(self):
        pass