import platform
from .client import MyComponent
from .factories import MacGuiFactory, WindowsGuiFactory

if __name__ == "__main__":
    WINDOWS = 'Windows'
    MAC = 'Darwin'

    my_os = platform.system()

    if my_os == WINDOWS:
        factory = WindowsGuiFactory()
    elif my_os == MAC:
        factory = MacGuiFactory()
    else:
        raise NotImplementedError()

    component = MyComponent(factory=factory)
    component.make()

    