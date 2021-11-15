from Criação.abstract_factory.products.button.windows_button import WindowsButton
from .abstract_factory import GUIAbstractFabrica

class WindowsGuiFactory(GUIAbstractFabrica):

    def create_window():
        return "[WINDOWS] - Criado um Window()"
    
    def create_button(x_point: int, y_point: int, height: int, width: int):
        return WindowsButton()