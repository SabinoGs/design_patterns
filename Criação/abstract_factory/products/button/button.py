from abc import ABC, abstractmethod

class Button(ABC):

    def __init__(self, title) -> None:
        self.title = title

    @abstractmethod
    def draw(self, x_point: int, y_point: int, width: int, height: int):
        return NotImplementedError