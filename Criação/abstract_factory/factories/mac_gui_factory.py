from Criação.abstract_factory.products.button.mac_button import MacButton
from .abstract_factory import GUIAbstractFabrica


class MacGuiFactory(GUIAbstractFabrica):

    def create_window():
        return "[MAC] - Criado um Window()"
    
    def create_button():
        return MacButton()