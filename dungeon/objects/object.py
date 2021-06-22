from abc import ABCMeta


class Object (metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def create(self):
        pass