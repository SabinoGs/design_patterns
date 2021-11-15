from .button import Button


class MacButton(Button):

    # Vamos assumir que os botões do MAC são desenhados de uma maneira diferente. Meio que de baixo pra cima.
    # Assim, a formula muda para: (y_point - heigth)
    def draw(self, x_point: int, y_point: int, width: int, height: int):
        return f"Drawing a MacButton on points: {x_point}, {y_point}, {x_point + width}, {y_point - height}"
