from abc import ABC, abstractmethod

class GUIAbstractFabrica(ABC):

    @abstractmethod
    def create_window():
        return NotImplementedError
    
    @abstractmethod
    def create_button():
        return NotImplementedError
