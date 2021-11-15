from .window import Window


class WindowsWindow(Window):

    def draw(self):
        points = f"{self.x}, {self.y}, {self.x + self.w}, {self.y + self.h}"
        return f"Drawing a WindowsWindow() on: {points}"