from .window import Window


class MacWindow(Window):

    # Assumindo novamente que os botões do MAC são desenhados de uma maneira diferente. Meio que de baixo pra cima.
    # Assim, a formula muda para: (y - h)
    def draw(self):
        points = f"{self.x}, {self.y}, {self.x + self.w}, {self.y - self.h}"
        return f"Drawing a WindowsWindow() on: {points}"