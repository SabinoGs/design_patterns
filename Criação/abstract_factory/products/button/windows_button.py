from .button import Button


class WindowsButton(Button):

    def draw(self, x_point: int, y_point: int, width: int, height: int):
        return f"Drawing a WindowsButton on points: {x_point}, {y_point}, {x_point + width}, {y_point + height}"
