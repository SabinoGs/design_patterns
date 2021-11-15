from .products.button.button import Button
from .products.window.window import Window
from .factories.abstract_factory import GUIAbstractFabrica

"""
Client é o utilizador dos componentes que definimos

Não é ele quem faz a instancia de qual fabrica utilizaremos, mas ele quem se beneficia de não saber qual é a fabrica.
Veja que nesse pedaço de código, não é possível saber se a fabrica utilizada é de Windows ou Mac. 

Só desejamos instanciar nossos componentes
""" 
class MyComponent():

    def __init__(self, factory: GUIAbstractFabrica) -> None:
        self.factory = factory

        self.button: Button = self.factory.create_button()
        self.window: Window = self.factory.create_window()

    def make(self):
        self.button.draw(x_point=10, y_point=20, width=5, height=10)
        self.window.draw(x_point=0, y_point=100, width=25, height=100)