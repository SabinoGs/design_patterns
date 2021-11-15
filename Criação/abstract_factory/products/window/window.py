from abc import ABC, abstractmethod


class Window(ABC):

    def __init__(self, title, x, y, w, h) -> None:
        self.title = title
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    @abstractmethod
    def draw(self):
        return NotImplementedError
